#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'hina'

# 多进程模式最大的优点就是稳定性高，因为一个子进程崩溃了，不会影响主进程和其他子进程

# 多进程模式的缺点是创建进程的代价大，在Unix/Linux系统下，用fork调用还行，
# 在Windows下创建进程开销巨大

# 在Windows下，多线程的效率比多进程要高

# 无论是多进程还是多线程，只要数量一多，效率肯定上不去

# 如果有几千个任务同时进行，操作系统可能就主要忙着切换任务，根本没有多少时间去执行任务了，
# 这种情况最常见的就是硬盘狂响，点窗口无反应，系统处于假死状态。

# 是否采用多任务的第二个考虑是任务的类型。我们可以把任务分为计算密集型和IO密集型
# 计算密集型任务的特点是要进行大量的计算，消耗CPU资源，
# 比如计算圆周率、对视频进行高清解码等等，全靠CPU的运算能力
# 于计算密集型任务，最好用C语言编写

# 第二种任务的类型是IO密集型，涉及到网络、磁盘IO的任务都是IO密集型任务，
# 这类任务的特点是CPU消耗很少，任务的大部分时间都在等待IO操作完成
# 对于IO密集型任务，任务越多，CPU效率越高，但也有一个限度
# 对于IO密集型任务，最合适的语言就是开发效率最高（代码量最少）的语言，脚本语言是首选，C语言最差

# 异步IO
# 现代操作系统对IO操作已经做了巨大的改进，最大的特点就是支持异步IO。
# 如果充分利用操作系统提供的异步IO支持，就可以用单进程单线程模型来执行多任务
# 这种全新的模型称为事件驱动模型

# Nginx就是支持异步IO的Web服务器，
# 它在单核CPU上采用单进程模型就可以高效地支持多任务。
# 在多核CPU上，可以运行多个进程（数量与CPU核心数相同），充分利用多核CPU。
# 由于系统总的进程数量十分有限，因此操作系统调度非常高效
# 用异步IO编程模型来实现多任务是一个主要的趋势

# 对应到Python语言，单进程的异步编程模型称为协程
