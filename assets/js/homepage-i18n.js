(() => {
  const translations = [
    ['.nav a[href="#about"]','关于我'], ['.nav a[href="#interests"]','研究兴趣'], ['.nav a[href="#news"]','最新动态'], ['.nav a[href="#research"]','精选研究'], ['.nav a[href="#contact"]','联系方式'],
    ['.bio','高效人工智能 · 多模态理解'], ['.affiliation strong','华南理工大学'], ['.affiliation span','中国 · 广州'],
    ['.profile-links a[href^="mailto:"]','电子邮箱'], ['.profile-links a[href*="xiaohongshu"]','小红书'], ['.profile-links a[href$=".pdf"]','个人简历'],
    ['.subtitle','本科研究者 · 华南理工大学'],
    ['#about h2','<span class="section-index">01</span> 关于我'],
    ['#about p:nth-of-type(1)','我是一名<strong>华南理工大学（SCUT）信息工程</strong>专业本科生（2023–2027）。'],
    ['#about p:nth-of-type(2)','我在<strong>中国科学院深圳先进技术研究院（SIAT, CAS）</strong>担任访问研究实习生，师从 <strong>Wenqi Fang 博士</strong>和<strong>博士生 Zhuoyu Wu</strong>，研究轻量化医学图像分割与高效预测细化。'],
    ['#about p:nth-of-type(3)','我也在<strong>香港中文大学（深圳）Ming Li 教授课题组</strong>担任访问研究实习生，协助开展孤独症儿童多模态行为评估研究。'],
    ['#about p:nth-of-type(4)','欢迎就研究、想法和潜在合作与我交流，也欢迎通过<a href="mailto:jingzhizhang569@gmail.com">电子邮件</a>联系我！'],
    ['#interests h2','<span class="section-index">02</span> 研究兴趣'],
    ['#interests p:nth-of-type(1)','我希望构建能够持续理解世界、实时辅助人们的<strong>高效交互式人工智能系统</strong>。驱动我研究的核心问题是：<strong>在计算资源有限的条件下，人工智能系统如何保留并更新真正重要的信息？</strong>'],
    ['#interests p:nth-of-type(2)','我此前的研究探索了医学图像分割中的轻量化架构与预测细化。在此基础上，我希望将高效人工智能拓展至<strong>流式多模态理解</strong>，探索系统如何长期维护有用的上下文、理解正在发生的交互，并在动态环境中作出恰当回应。'],
    ['#interests p:nth-of-type(3)','长远来看，我希望开发能够从连续感官输入中学习、在日常生活中帮助人们的人工智能助手，尤其关注<strong>及时性、效率和得体的交互</strong>。'],
    ['.research-topics span:nth-child(1)','高效人工智能'], ['.research-topics span:nth-child(2)','流式多模态理解'], ['.research-topics span:nth-child(3)','交互智能'],
    ['#news h2','<span class="section-index">03</span> 最新动态'],
    ['.news li:nth-child(1) span','加入<strong>香港中文大学（深圳）</strong>担任访问研究实习生，参与多模态行为评估研究。'],
    ['.news li:nth-child(2) span','<strong>Gain-Aware Controller</strong> 被 <strong>ICONIP 2026</strong> 接收。'],
    ['.news li:nth-child(3) span','<strong>RIGS-Refiner</strong> 被 <strong>APSIPA ASC 2026</strong> 接收，并入选<strong>口头报告</strong>。'],
    ['.news li:nth-child(4) span','加入<strong>中科院深圳先进院</strong>担任访问研究实习生，研究超轻量级医学人工智能。'],
    ['#research h2','<span class="section-index">04</span> 精选研究'],
    ['.paper:nth-child(1) h3 a','基于增益感知预测空间递归控制器的轻量化息肉分割'],
    ['.paper:nth-child(1) p','提出一个即插即用的 189 参数息肉分割模块，通过跟踪预测差异和不确定性细化分割结果，在不改变模型架构的情况下，于七种骨干网络上取得稳定提升。'],
    ['.paper:nth-child(1) .author','第一作者'], ['.paper:nth-child(1) .venue','ICONIP 2026 · 已接收'],
    ['.paper:nth-child(2) h3 a','RIGS-Refiner：用于结肠镜息肉分割的风险引导预测空间递归细化'],
    ['.paper:nth-child(2) p','提出一个 519 参数的轻量插件，利用预测空间先验进行风险引导的选择性修复，在分割细化中优于计算开销更高的后处理方法。'],
    ['.paper:nth-child(2) .author','第一作者'], ['.paper:nth-child(2) .venue','APSIPA ASC 2026 <b class="oral">口头报告</b>'],
    ['.paper:nth-child(1) .paperlink','论文 ↗'], ['.paper:nth-child(2) .paperlink','论文 ↗'],
    ['.paper:nth-child(1) .figure span','查看大图 ↗'], ['.paper:nth-child(2) .figure span','查看大图 ↗'],
    ['#miscs h2','<span class="section-index">05</span> 生活点滴'],
    ['.misc li:nth-child(1)','曾任<strong>华南理工大学（EE）艺术团团长</strong>，很享受与热爱表演的伙伴们相聚。'],
    ['.misc li:nth-child(2)','我是<strong>方大同</strong>的忠实乐迷，也喜欢唱歌（虽然可能主要是在淋浴时）。'],
    ['.misc li:nth-child(3)','我是<strong>斯蒂芬·库里</strong>的支持者，也经常打篮球和乒乓球。'],
    ['#contact h2','<span class="section-index">06</span> 联系我'], ['#contact p','欢迎就研究、想法或潜在合作与我交流。'],
    ['.contacts a[href^="mailto:"]','电子邮箱'], ['.contacts a[href*="xiaohongshu"]','小红书 ↗'], ['.contacts a[href$=".pdf"]','下载简历 ↓'], ['.foot','© Jiachi Zhang · 中国广州']
  ];
  const entries = translations.map(([selector, zh]) => {
    const element = document.querySelector(selector);
    return element ? { element, en: element.innerHTML, zh } : null;
  }).filter(Boolean);
  const buttons = [...document.querySelectorAll('[data-language]')];
  const setLanguage = language => {
    const selected = language === 'zh' ? 'zh' : 'en';
    entries.forEach(entry => { entry.element.innerHTML = entry[selected]; });
    document.documentElement.lang = selected === 'zh' ? 'zh-CN' : 'en';
    document.querySelector('.nav').setAttribute('aria-label', selected === 'zh' ? '主导航' : 'Main navigation');
    document.querySelector('.modal').setAttribute('aria-label', selected === 'zh' ? '论文图片' : 'Research figure');
    document.querySelector('.modal-close').setAttribute('aria-label', selected === 'zh' ? '关闭图片' : 'Close figure');
    buttons.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.language === selected)));
    try { localStorage.setItem('homepage-language', selected); } catch (_) {}
  };
  buttons.forEach(button => button.addEventListener('click', () => setLanguage(button.dataset.language)));
  let saved = 'en';
  try { saved = localStorage.getItem('homepage-language') || 'en'; } catch (_) {}
  setLanguage(saved);
})();
