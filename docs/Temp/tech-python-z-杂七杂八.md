## This cd.sh is to backup shell script of https://jenkins7.svc.eng.vmware.com/job/OSM-cicd/job/osm-client-publish/configure
set -e

# set `TEST` at https://jenkins7.svc.eng.vmware.com/job/OSM-cicd/job/osm-client-publish/configure -> Bindings -> Inject environment variables to the build process -> Properties Content
TEST=$TEST

if [ $TEST != true ]; then
        ARTIFACTORY_PUBLISH_REPO="https://artifactory.eng.vmware.com/artifactory/osm-client-generic-local/publish"
        TARGET_BRANCH="master_python3"
else
        # Change these variables when you test
        ARTIFACTORY_PUBLISH_REPO=$ARTIFACTORY_PUBLISH_REPO_FOR_TEST
        TARGET_BRANCH=$TARGET_BRANCH_FOR_TEST
fi

username=$artifactory_username
password=$artifactory_password

OSSTPCLIENTS3_REPO='osstpclients3'
OSSTPCLIENTS3_LINUX_REPO='osstpclients3-linux'
OSSTPCLIENTS3_MAC_REPO='osstpclients3-mac'
OSSTPCLIENTS3_WINDOWS_REPO='osstpclients3-windows'

EXISTING_OSSTPCLI_LATEST_VERSION=$(curl -G -d 'g=publish' -d 'a=osstpclients3' -d 'repos=osm-client-generic-local'  https://artifactory.eng.vmware.com/api/search/latestVersion)

cd /home/scotzilla/osstpmgt/clients/
git checkout $TARGET_BRANCH
git reset --hard HEAD
git pull

NEW_OSSTPCLI_VERSION=$(python3 -c 'import settings;\
                      print(settings.VERSION)')

# Param `archive_path` has to be absolute path
upload_file_to_artifactory() {
        # ↓ e.g. if archive_path is `/Users/vzhong/xx.zip`, then archive_name will be `xx.zip`
        archive_path=$1
        archive_name=${archive_path##*/}

        artifactory_path=$2

        # If tarball or zip already exists, skip pushing.
        ret_code=$(curl -o /dev/null --silent -Iw '%{http_code}' "${artifactory_path}")
        if [ $ret_code = 404 ]; then
                echo "Pushing $archive_name to artifactory..."
                curl -u $username:$password -XPUT $artifactory_path -T $archive_path
        else
                echo "--------------- WARNNING!!! --------------"
                echo "Skiped pushing tarball $archive_name, due $artifactory_path is already existing in artifactory, please check artifactory to confirm it!"
                echo "------------------------------------------"
        fi
}

assert_no_same_version_existing_in_artifactory() {
        artifactory_path=$ARTIFACTORY_PUBLISH_REPO/$OSSTPCLIENTS3_REPO/$OSSTPCLIENTS3_REPO-$NEW_OSSTPCLI_VERSION.zip
        ret_code=$(curl -o /dev/null --silent -Iw '%{http_code}' "${artifactory_path}")
        if [ $ret_code != 404 ]; then
                echo "Failed, osstpclients version $NEW_OSSTPCLI_VERSION is already exists in artifactory repo: $ARTIFACTORY_PUBLISH_REPO, you have to update variable `VERSION` in settings.py to publish a newer version."
                exit 1;
        fi
}

assert_no_same_version_existing_in_artifactory

git checkout $TARGET_BRANCH

echo "--- build.sh start to build Linux、windows version... ---"
./build.sh
echo "--- build.sh finished ---"

# To make sure that no errors accurred during `./build.sh` process
cd /home/scotzilla/osstpmgt/clients/bin/client_executables/linux-amd64
./osstp-load -h > /tmp/osstp-load.log
if ! grep -iq 'usage: osstp-load' /tmp/osstp-load.log;then
        echo "--------------- ERROR!!! --------------"
        echo "osstp-load is not runable, because of `./build.sh` failed."
        echo "------------------------------------------"
        exit 1;
fi

echo "--- trigger buildweb to build bins for mac ---"
cd /home/scotzilla/osstpmgt/clients/
export MR_BRANCH=$TARGET_BRANCH
DOWNLOAD_DELIVERABLE_TARBALL_AS=/tmp/clients3_mac_$NEW_OSSTPCLI_VERSION.tar.bz2
DOWNLOAD_DELIVERABLE_ZIP_AS=/tmp/clients3_mac_$NEW_OSSTPCLI_VERSION.zip
export DOWNLOAD_DELIVERABLE_TARBALL_AS=$DOWNLOAD_DELIVERABLE_TARBALL_AS
export DOWNLOAD_DELIVERABLE_ZIP_AS=$DOWNLOAD_DELIVERABLE_ZIP_AS
# MR_BRANCH, DOWNLOAD_DELIVERABLE_TARBALL_AS, DOWNLOAD_DELIVERABLE_ZIP_AS are used by build_bins_for_mac.py
python3 build_bins_for_mac.py
echo "--- build finished ---"


# --- Upload linux-amd64 executable to artifactory ---
cd /home/scotzilla/osstpmgt/clients/bin/client_executables/linux-amd64
# tarball
archive_path=/tmp/clients3_linux_amd64_$NEW_OSSTPCLI_VERSION.tar.bz2
artifactory_file_path=$ARTIFACTORY_PUBLISH_REPO/$OSSTPCLIENTS3_LINUX_REPO/$OSSTPCLIENTS3_LINUX_REPO-$NEW_OSSTPCLI_VERSION.tar.bz2
tar cvjf $archive_path *
upload_file_to_artifactory $archive_path $artifactory_file_path
# zip
archive_path=/tmp/clients3_linux_amd64_$NEW_OSSTPCLI_VERSION.zip
artifactory_file_path=$ARTIFACTORY_PUBLISH_REPO/$OSSTPCLIENTS3_LINUX_REPO/$OSSTPCLIENTS3_LINUX_REPO-$NEW_OSSTPCLI_VERSION.zip
/build/toolchain/lin64/zip-2.32/bin/zip -r $archive_path *
upload_file_to_artifactory $archive_path $artifactory_file_path

# --- Upload windows-amd64 executable to artifactory ---
cd /home/scotzilla/osstpmgt/clients/bin/client_executables/windows-amd64
# tarball
archive_path=/tmp/clients3_windows_amd64_$NEW_OSSTPCLI_VERSION.tar.bz2
artifactory_file_path=$ARTIFACTORY_PUBLISH_REPO/$OSSTPCLIENTS3_WINDOWS_REPO/$OSSTPCLIENTS3_WINDOWS_REPO-$NEW_OSSTPCLI_VERSION.tar.bz2
tar cvjf $archive_path *
upload_file_to_artifactory $archive_path $artifactory_file_path
# zip
archive_path=/tmp/clients3_windows_amd64_$NEW_OSSTPCLI_VERSION.zip
artifactory_file_path=$ARTIFACTORY_PUBLISH_REPO/$OSSTPCLIENTS3_WINDOWS_REPO/$OSSTPCLIENTS3_WINDOWS_REPO-$NEW_OSSTPCLI_VERSION.zip
/build/toolchain/lin64/zip-2.32/bin/zip -r $archive_path *
upload_file_to_artifactory $archive_path $artifactory_file_path

# --- Upload mac executable to artifactory ---
# tarball
artifactory_file_path=$ARTIFACTORY_PUBLISH_REPO/$OSSTPCLIENTS3_MAC_REPO/$OSSTPCLIENTS3_MAC_REPO-$NEW_OSSTPCLI_VERSION.tar.bz2
upload_file_to_artifactory $DOWNLOAD_DELIVERABLE_TARBALL_AS $artifactory_file_path
# zip
artifactory_file_path=$ARTIFACTORY_PUBLISH_REPO/$OSSTPCLIENTS3_MAC_REPO/$OSSTPCLIENTS3_MAC_REPO-$NEW_OSSTPCLI_VERSION.zip
upload_file_to_artifactory $DOWNLOAD_DELIVERABLE_ZIP_AS $artifactory_file_path

# --- Upload osstpclients3 source code to artifactory ---
cd /home/scotzilla/osstpmgt/clients/
# tarball
archive_path=/tmp/osstpclients3_$NEW_OSSTPCLI_VERSION.tar.bz2
artifactory_file_path=$ARTIFACTORY_PUBLISH_REPO/$OSSTPCLIENTS3_REPO/$OSSTPCLIENTS3_REPO-$NEW_OSSTPCLI_VERSION.tar.bz2
tar cvjf $archive_path bin etc lib src settings.py
upload_file_to_artifactory $archive_path $artifactory_file_path
# zip
archive_path=/tmp/osstpclients3_$NEW_OSSTPCLI_VERSION.zip
artifactory_file_path=$ARTIFACTORY_PUBLISH_REPO/$OSSTPCLIENTS3_REPO/$OSSTPCLIENTS3_REPO-$NEW_OSSTPCLI_VERSION.zip
/build/toolchain/lin64/zip-2.32/bin/zip -r $archive_path bin etc lib src settings.py
upload_file_to_artifactory $archive_path $artifactory_file_path

echo "---------------------------- Finished ------------------"
