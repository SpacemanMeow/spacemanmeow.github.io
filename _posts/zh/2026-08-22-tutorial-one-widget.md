---
layout: post
title: "One Widget 官方使用指南"
date: 2026-08-22 09:00:00 +0800
categories: [Tutorial]
tags: [Home Screen Widgets, KWGT, One Widget]
lang: zh
author: author_meow_id
last_modified_at: 2026-11-05
description: "一份完整的 One Widget 使用指南——放入四种风格的 500+ 桌面小组件，配置尺寸与透明度，添加快捷开关与应用快捷方式。"
image: /assets/images/apps/one-widget/icon.webp
---

## 目录

- [应用简介](#应用简介)
- [首次使用](#首次使用)
- [浏览四种风格](#浏览四种风格)
- [添加组件](#添加组件)
- [配置组件](#配置组件)
- [快捷开关](#快捷开关)
- [应用快捷方式](#应用快捷方式)
- [实时信息组件](#实时信息组件)
- [设置](#设置)
- [典型场景](#典型场景)
- [常见问题](#常见问题)

## 应用简介

One Widget 内置 **500+ 可自定义安卓[主屏组件](/zh/glossary/what-is-a-home-screen-widget/)**，横跨四种流行风格，外加应用快捷方式与快捷开关。它是一款 **无需账号的小组件 app**：浏览四种风格库、摆上一个预设，再改尺寸、背景色与圆角即可。这份指南会走完从首次启动、四种风格，到添加与配置组件、快捷开关，再到时钟、日历与电量实时信息的完整流程。

**🎨 四种风格**
- **One UI**（默认；免费"精简"版应用包含的唯一样式）
- **Nothing**
- **Glass**
- **Material You**

> 这里的"Material You"是一个使用固定蓝/紫昼夜色板的 *风格名*——并非安卓 12 基于壁纸的动态配色。

**⚡ 快捷开关**
- 11 个开关：蓝牙、移动数据、Wi-Fi、手电筒、旋转、飞行模式、热点、勿扰、定位、振动、深色模式

**📱 应用快捷方式与联系人**
- 你应用与电话/拨号的一步启动器

**📊 实时信息**
- 时钟、日历、电池与 RAM 组件就地更新

**💲 两个应用，而非一个**
- 一个 **免费"精简"应用**（仅 One UI 风格）与一个 **付费"完整"应用**（全部四种风格）。没有应用内购买——从 Google Play 安装完整应用即解锁一切。

## 首次使用

打开 One Widget 进入 4 标签画廊：**One UI / Nothing / Glass / Material You**。

- 每个风格页列出分类：工具、入口、硬件、时钟、启动器、组合、便签、联系人
- 点分类看组件预览

![One UI 风格小组件预设](/assets/images/blog/tutorial_widget_one_ui.webp){: width="180" .normal }
![Nothing 风格小组件点阵预设](/assets/images/blog/tutorial_widget_nothing.webp){: width="180" .normal }
![玻璃风格小组件通透预设](/assets/images/blog/tutorial_widget_glass.webp){: width="180" .normal }
![Material You 小组件配色预设](/assets/images/blog/tutorial_widget_material.webp){: width="180" .normal }

## 浏览四种风格

切换顶部标签预览每种风格。**One UI** 是默认，且在免费精简应用中可用；Nothing / Glass / Material You 需要付费完整应用。

## 添加组件

1. 长按主屏 → **组件**
2. 在列表中找到 **One Widget** 并选一个变体
3. 系统打开 One Widget **配置** 界面
4. 设定选项并点 **确认** 放置

![把安卓小组件添加到主屏](/assets/images/blog/tutorial_widget_add.webp){: width="180" .normal }

## 配置组件

多数组件共享通用选项：

- **主题色**（弹出调色板）
- **深色 / 浅色** 模式
- **形状**——圆形或圆角矩形
- **大小**——网格选项如 1x1、2x1、4x1、5x1、6x1、2x2、4x2、5x2、6x2（最大 **6x2**）

图标背景色与圆角半径由形状派生（圆形 = 边长/2，圆角 = 边长/3）。

![配置自定义小组件的尺寸、颜色与圆角](/assets/images/blog/tutorial_widget_config.webp){: width="180" .normal }

## 快捷开关

1. 从开关组件选择开关类型（Wi-Fi、蓝牙、手电筒、旋转、勿扰……）
2. 放置单个开关，或用 **组合 4x1** 组件把最多 5 个开关放进一条（默认：蓝牙 / Wi-Fi / 移动数据 / 手电筒 / 旋转）
3. 点开关执行：
   - **手电筒** 实际切换闪光灯（`CameraManager`）
   - **Wi-Fi / 蓝牙 / 勿扰** 打开相应系统设置界面
   - **旋转** 写入系统自动旋转设置

## 应用快捷方式

1. 配置一个 **应用快捷方式** 组件
2. 在每个槽从启动器列表选一个已装应用
3. 点组件启动该应用（若未安装则打开 Google Play）

## 实时信息组件

- **时钟** 组件按系统组件更新周期（每 30 分钟）与尺寸变化时重绘
- **电池 / RAM** 组件约每 **60 秒** 轮询设备状态；电池也会从电量变化广播即时更新
- 日历 / 便签组件为静态或在 30 分钟周期刷新

## 设置

设置包含深色模式、语言、温度单位、评分、分享、反馈、隐私与版本。

## 典型场景

- **5 分钟焕新主屏**——打开四标签画廊，点一个风格，挑个时钟或天气组件，摆上去；无需编辑器、无需 Kode。
- **配壁纸**——设主题色与深/浅色，选圆形或圆角，组件融入你的启动器。
- **一键快捷开关**——把 Wi-Fi、蓝牙、手电筒放进 4x1 一条，不再翻设置。
- **应用与联系人快捷方式**——从单个组件启动 Chrome、地图或常用联系人。
- **全安卓设备**——Galaxy、Pixel、Nothing 都支持；免费精简版含 One UI 风格，完整版解锁四种。

## 常见问题

### 为什么免费应用里用不了 Nothing / Glass / Material You？
免费应用是只包含 One UI 风格的"精简"构建。安装付费完整应用解锁另外三种风格。

### "Material You" 是真的动态主题吗？
它是一种使用固定蓝/紫昼夜色板的风格。并非基于壁纸的动态配色。

### 开关需要 root 吗？
不需要。它们使用标准系统 API 与设置；手电筒用相机闪光灯 API。

## 小结

One Widget 是给你的安卓主屏最快拥有时尚、一体机式组件工具箱的方式——四种外观数百个组件，外加快捷开关与应用快捷方式。

## 相关术语

- [什么是主屏幕小组件（Home Screen Widget）？](/zh/glossary/what-is-a-home-screen-widget/)
- [什么是 Material You？](/zh/glossary/what-is-material-you/)
- [什么是 Nothing UI？](/zh/glossary/what-is-nothing-ui/)
- [什么是 Galaxy One UI？](/zh/glossary/what-is-galaxy-one-ui/)
- [什么是 iOS Glass？](/zh/glossary/what-is-ios-glass/)
