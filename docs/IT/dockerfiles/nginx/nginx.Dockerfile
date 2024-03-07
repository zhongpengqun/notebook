FROM harbor-repo.vmware.com/dockerhub-proxy-cache/library/nginx:1.25.1

# ↓ failed，shows by `service nginx status`
#CMD service nginx start

# ↓ also failed，shows by `service nginx status`
#RUN service nginx restart && service nginx status
#CMD nginx "-g daemon off;"

# run cmd `service nginx start` inside container manually