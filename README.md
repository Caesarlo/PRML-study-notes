# 📖 PRML 学习笔记

> **Pattern Recognition and Machine Learning**
> Christopher M. Bishop, Springer, 2006

[![进度](https://img.shields.io/badge/进度-Chapter%201-blue?style=flat-square)](./PRML)
[![笔记工具](https://img.shields.io/badge/工具-Obsidian-7C3AED?style=flat-square&logo=obsidian&logoColor=white)](https://obsidian.md)
[![语言](https://img.shields.io/badge/语言-Python%203-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)

---

## 关于本书

PRML 是机器学习领域最经典的教材之一，系统覆盖了从概率论基础到深度模型的完整知识体系。全书以**贝叶斯视角**贯穿始终，强调原理推导而非黑盒调参。

```
适合人群：有一定线性代数、概率论基础，希望深入理解 ML 原理的读者
难度曲线：★★★★☆  前几章平缓，第 8 章（图模型）后陡增
代码语言：Python (NumPy / Matplotlib / scikit-learn)
```

---

## 章节目录

| # | 章节 | 核心概念 | 笔记 | 状态 |
|---|------|----------|------|------|
| 1 | Introduction | 模式识别、多项式拟合、概率论、信息论 | [📂](./Ch01%20-%20Introduction) | 🔵 进行中 |
| 2 | Probability Distributions | 高斯分布、指数族、非参数方法 | — | ⬜ 待开始 |
| 3 | Linear Models for Regression | 贝叶斯线性回归、模型选择、证据近似 | — | ⬜ 待开始 |
| 4 | Linear Models for Classification | 判别函数、生成式/判别式模型、Laplace 近似 | — | ⬜ 待开始 |
| 5 | Neural Networks | MLP、反向传播、正则化、贝叶斯神经网络 | — | ⬜ 待开始 |
| 6 | Kernel Methods | 核函数、高斯过程 | — | ⬜ 待开始 |
| 7 | Sparse Kernel Machines | SVM、相关向量机 RVM | — | ⬜ 待开始 |
| 8 | Graphical Models | 贝叶斯网络、马尔可夫随机场、因子图、消息传递 | — | ⬜ 待开始 |
| 9 | Mixture Models and EM | GMM、EM 算法、变分 EM | — | ⬜ 待开始 |
| 10 | Approximate Inference | 变分推断、变分 Bayes、EP | — | ⬜ 待开始 |
| 11 | Sampling Methods | MCMC、Metropolis-Hastings、Gibbs 采样 | — | ⬜ 待开始 |
| 12 | Continuous Latent Variables | PCA、概率 PCA、独立成分分析 ICA | — | ⬜ 待开始 |
| 13 | Sequential Data | HMM、卡尔曼滤波、粒子滤波 | — | ⬜ 待开始 |
| 14 | Combining Models | Boosting、条件混合模型 | — | ⬜ 待开始 |

---

## Chapter 1 笔记索引

```
Ch01 - Introduction/
├── 1.0 模式识别与机器学习概览.md   监督/无监督/强化学习的基本框架
└── 1.1 多项式曲线拟合.md           过拟合、正则化、模型选择的直觉入门
```

**Chapter 1 知识地图**

```
模式识别
├── 监督学习 ──────────── 分类 / 回归
├── 无监督学习 ─────────── 聚类 / 密度估计 / 降维
└── 强化学习 ──────────── 探索 vs 利用 / 信用分配

1.1 多项式曲线拟合
├── 最小二乘 ──────────── E(w) = ½Σ[y(xₙ,w) - tₙ]²
├── 过拟合 ─────────────── M↑ → 训练误差↓ / 测试误差↑
└── 正则化（岭回归）────── Ẽ(w) = E(w) + λ/2·‖w‖²

1.2 概率论回顾（待更新）
├── 加法规则 / 乘法规则
├── 贝叶斯定理
└── 高斯分布

1.3 模型选择（待更新）
1.4 维度灾难（待更新）
1.5 决策论（待更新）
1.6 信息论（待更新）
```

---

## 环境配置

```bash
pip install numpy matplotlib scikit-learn jupyter
```

笔记中的代码均可独立运行，图片输出到各章节的 `assets/` 目录。

---

## 参考资源

- 📄 [官方书页（Springer）](https://www.springer.com/book/9780387310732)
- 🎥 [Bishop 本人的讲座视频（微软研究院）](https://www.microsoft.com/en-us/research/video/pattern-recognition-machine-learning/)
- 💻 [PRML 代码实现参考（prml-python）](https://github.com/ctgk/PRML)
- 📝 [习题解答参考](https://github.com/zhengqigao/PRML-Solution-Manual)

---

<p align="center">
  <sub>持续更新中 · 笔记工具：Obsidian · 2025</sub>
</p>
