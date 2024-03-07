# Angular
- angular vs angularJs
- What's the relationship between angular and Typescript ?

# Typescript
- online playground https://www.typescriptlang.org/play


- .component.ts
    - `.ts` 文件
        - ts 应该是表示 typescript

- npm install


```
Error from chokidar (/xxx/yyy): Error: ENOSPC: System limit for number of file watchers reached, watch '/hxxx/favicon.ico'

s:

$ echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf
```

```
Error: ENOENT: no such file or directory, scandir '/home/hartron/foodnetteam/codebase/mandi/node_modules/node-sass/vendor'

s:

$ npm rebuild node-sass
```

- subscribe

- ===

- ngOnInit

- Install ng
```
sudo npm install -g @angular/cli
```


"Yarn 是为了弥补 npm 的一些缺陷而出现的"


- dependency injection

- node_modules
    - `You can think of the node_modules folder like a cache for the external modules that your project depends upon`

- .bowerrc
    - 

- EditorConfig

- eslintrc
    - `ESLint is a static code analysis tool for identifying problematic patterns found in JavaScript code.`

- angular.json

- package-lock.json & package.json
    - 默认，当我们在一个项目中npm install时候（前提该项目有package.json文件），安装完成后，会自动生成一个package-lock.json文件（位置和之前的package.json文件同级）
    - 该文件里面记录了package.json依赖的模块，以及依赖的依赖
    - 如果你有浏览它，会发现它长得类似package.json的依赖，但是比它复杂多了

- dependencies & devDependencies
    - devDependencies下列出的模块，是我们开发时用的依赖项，像一些进行单元测试之类的包，比如jest，我们用写单元测试，它们不会被部署到生产环境。dependencies下的模块，则是我们生产环境中需要的依赖，即正常运行该包时所需要的依赖项。
    - 后面的package-lock.json 中的 dependencies 对应的就是package.json中的 dependencies


- @angular/cli
    - `在使用 Angular CLI 之前，你必须确保系统中 Node.js 的版本高于 6.9.0 且 npm 的版本高于 3.0.0。`
        - node.js 与 angular的关系 ？
            - 与AngularJS不同，NodeJS是一个服务器端框架
        - npm 与 angular/cli的关系 ？
            - npm 安装 angular/cli  `npm i @angular/cli –save-dev`
            - NPM contains and manages many packages and modules, and NG is one such module
            - You can start, load compile your app using npm which internally use or load ng module if it is an angular projec

    - 安装完成后用 `$ ng version` 查看是否安装成功

- karma.conf.js

- tsconfig.spec.json

- <router-outlet></router-outlet>

- app.module.ts
    - APPMODULE: THE ROOT MODULE; Tell Angular how to construct and bootstrap the app in the root "AppModule".
        - https://v2.angular.io/docs/ts/latest/guide/appmodule.html
    
