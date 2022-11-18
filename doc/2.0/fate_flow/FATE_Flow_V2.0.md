## FATE FLOW V2.0方案



### 1. 背景

- 联邦学习为打破“数据孤岛”而生，然而随着越来越多的机构投身到联邦学习领域，不同架构的联邦学习系统之间逐渐形成了新的“孤岛”现象，互联互通显得越发重要。FATE FLow 2.0版本将定义全新的Open Flow Api，从流程调度和算法调度两个层面实现互联互通。

	
- 在流程调度方面，将使用标准化的作业与任务协同调度接口。由于隐私计算是一个涉及双方数据协同的运算过程，在互联互通的过程中会涉及双方网络传输以及异步运算等关键步骤，网络延迟或者计算资源调度异常都会导致隐私计算任务等待或者失败，因此在异构情况下，需要标准化的调度方案，使用标准化的作业与任务协同接口，来统一协调异构双方隐私计算任务的执行。


- 在算法调度方面，将引入“算法容器”加载算法。算法是隐私计算的核心，而算法的加载就是用来使用标准化的接口或方式管理异构算法，其实现方式决定了算法的可扩展性和易扩展性，并且其设计方式也会影响到算法的执行效率。因此，需要制定统一的算法镜像构建标准与接口并定义一套规范的镜像加载机制与流程，从而保证整个算法容器加载过程的安全、高效及高可用。

### 2. 整体方案图

![image-20220922195625843](../images/open_flow.png)

### 3. 调度层

#### 3.1 实体定义

说明：所有调度系统对实体定义需一致

##### 3.1.1 流程（pipeline）

采用DAG结构定义的、可编排的隐私计算作业运行模板，用于描述一组组件的上下游及依赖关系。

##### 3.1.2 资源（resource）

一个隐私计算流程的作业在运行时可使用的硬件资源信息，调度层会根据此配置信息来为每个组件的任务实例分配运行时的配置。

##### 3.1.3 作业（job）

一个隐私计算流程在经过运行参数配置后的运行实例，通常包含参与方节点信息、参与方资源、若干任务排列的集合等。

##### 3.1.4 任务（task）

每个组件运行的实例，每个任务通常包含有组件的输入、输出、运行的参数等。

##### 3.1.5 组件（component）

独立执行隐私计算任务的功能模块单元，其经过封装、符合开放接口规范、可以完成某个隐私计算功能，可独立部署，并被使用在隐私计算流程DAG中，用顶点(vertex)表示。

#### 3.2 流程调度时序图

说明：1.x版本的发起方即为调度方，与此不同的是新版本计划将调度逻辑脱离，调度方由任务配置决定，可以为发起方、合作方和第三方。

##### 3.2.1 push模式

![image-20220922195625843](../images/push.png)



##### 3.2.1 pull模式

![image-20220922195625843](../images/pull.png)

#### 3.3 应用层

- 说明：用于对接上层系统
- [应用层接口定义文档](./manage_api.md)

#### 3.4 底座层

- 说明：用于对接算法容器
- [底座层接口定义文档](./task_callback_api.md)

#### 3.5 互联互通层

- 说明：用于对接跨机构、站点调度

- [互联互通层接口定义文档](./open_flow_api.md)


### 4. 算法容器调度(南北向)

说明：FATE历史版本中的算法加载是以python脚本形式在subprocess进程中加载，在安全性、扩展性等方面存在不足，且无法满足异构算法组合编排场景。在2.0版本计划引入“算法容器”加载算法，通过制定统一的算法镜像构建标准与接口并定义一套规范的镜像加载机制与流程，实现异构场景的互联互通。

![image-20220922195625843](../images/federationml_schedule.png)

注：图中节点A、B代表两家隐私计算提供商，A-X代表A厂的算法X，B-Y代表B厂算法Y。

#### 4.1 容器注册与加载

- [算法容器注册与加载文档](./docker_load.md)

#### 4.2 平台资源

##### 4.2.1 通信

- [通信api](../federation/federation_api.md)

##### 4.2.2 计算

- [计算api](../computing/computing_api.md)

##### 4.2.3 存储

- [存储api](../storage/storage_api.md)

### 5. DAG定义
fate 2.0版本计划在DAG的结构定义方面进行调整，主要包括节点信息、组件参数、资源参数等等。

### 6. 解耦

fate 1.x版本的调度层与算法层在数据、模型、类调用等方面存在一些耦合和特判的情况。在fate 2.0版本， 会在算法和调度层面做解偶工作，以此降低异构算法接入的开发成本。

### 7. 资源管控
- 资源类型
- 管控粒度

### 8. 状态码定义
- [api返回码]()
- [job失败码]()



