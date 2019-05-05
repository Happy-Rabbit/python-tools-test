## 这个项目是用来编写python3的工具的

### 目前的工具列表如下

- printf(info, end='\n', mode='common', delayTime=0)

---

## V 0.0.2

---

### 工具列表如下

- printf(info, end='\n', mode='common', delayTime=0)

### 新增了参数 ```end```

** ```printf()``` 新增函数(第四个) -- end **

```end``` 用于在行位增加特定字符, 作用等同于 ```print()``` 里的参数 ```end```

---

## V 0.0.1

---

### 工具列表如下

- printf(info, mode='common', delayTime=0)

#### printf用法

** ```printf()``` 第一个参数 -- info **

```info```, 很简单, 就是需要显示在窗口上的信息

** ```printf()``` 第二个参数 -- mode **

```mode``` 有两种形式, 一个是普通显示('common'), 另一个是延迟显示('delay'), 默认情况下是普通显示

- 普通显示就是正常显示, 和自带函数 ```print``` 没啥区别
- 延迟显示需要调用 ```time.sleep()``` 和 ```sys.stdout.flush()```. ```time.sleep()``` 用来延迟输出, ```sys.stdout.flush()``` 则是用来刷新缓冲区.

** ```printf()``` 第三个参数 -- delayTime **

```delayTime``` 是作为存储延迟显示时间而存在的, 它的单位是毫秒, 如果 ```mode``` 是 'common' 的话, ```delayTime``` 写不写都无所谓, 如果 ```mode``` 是 'delay' 模式, 则 ```delayTime``` 此时被用来存储延时时间.
