(() => {
  const translations = [
    ['.nav a[href="#about"]','关于我'], ['.nav a[href="#interests"]','研究兴趣'], ['.nav a[href="#news"]','最新动态'], ['.nav a[href="#research"]','精选研究'], ['.nav a[href="#contact"]','联系方式'],
    ['.bio','高效人工智能 · 多模态理解'], ['.affiliation strong','华南理工大学'], ['.affiliation span','中国 · 广州'],
    ['.profile-links a[href^="mailto:"]','电子邮箱'], ['.profile-links a[href$=".pdf"]','个人简历'],
    ['.brand','张伽弛'], ['.sidebar h1','张伽弛'], ['.intro-name','张伽弛'],
    ['.subtitle','本科生 · 华南理工大学'],
    ['#affiliations h2','所在机构'],
    ['.institution:nth-child(1) h3','华南理工大学'], ['.institution:nth-child(1) p','本科生 · 信息工程'],
    ['.institution:nth-child(2) h3','中国科学院深圳先进技术研究院'], ['.institution:nth-child(2) p','访问研究实习生'],
    ['.institution:nth-child(3) h3','香港中文大学（深圳）'], ['.institution:nth-child(3) p','访问研究实习生'],
    ['#about h2','<span class="section-index">01</span> 关于我'],
    ['#about p:nth-of-type(1)','我目前就读于<strong>华南理工大学（SCUT）信息工程专业</strong>，本科在读（2023–2027）。'],
    ['#about p:nth-of-type(2)','我目前在<strong>中国科学院深圳先进技术研究院（SIAT, CAS）</strong>担任访问研究实习生，在 <strong>Wenqi Fang 博士</strong>和<strong>博士生 Zhuoyu Wu</strong> 的指导下，研究轻量化医学图像分割与预测结果细化。'],
    ['#about p:nth-of-type(3)','我也在<strong>香港中文大学（深圳）Ming Li 教授课题组</strong>担任访问研究实习生，参与孤独症儿童多模态行为评估相关研究。'],
    ['#about p:nth-of-type(4)','欢迎就研究、想法和潜在合作与我交流，也欢迎通过<a href="mailto:jingzhizhang569@gmail.com">电子邮件</a>联系我！'],
    ['#interests h2','<span class="section-index">02</span> 研究兴趣'],
    ['#interests p:nth-of-type(1)','我希望构建<strong>高效、可交互的人工智能系统</strong>，让它们能够持续理解周围环境，并及时为人们提供帮助。我关心的一个核心问题是：<strong>在计算资源有限的情况下，系统该如何保留和更新真正重要的信息？</strong>'],
    ['#interests p:nth-of-type(2)','此前，我主要研究医学图像分割中的轻量化模型和预测细化方法。接下来，我希望把高效人工智能的思路拓展到<strong>流式多模态理解</strong>：探索系统如何在持续交互中维护有用的上下文、理解正在发生的事情，并在动态环境中作出合适的回应。'],
    ['#interests p:nth-of-type(3)','长远来看，我希望开发能够持续感知环境、帮助人们处理日常事务的人工智能助手，并关注它们的<strong>响应时机、运行效率和交互方式</strong>。'],
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
    ['.misc li:nth-child(2)','喜欢<strong>方大同</strong>的音乐，也喜欢唱歌（虽然大多是在洗澡的时候）。'],
    ['.misc li:nth-child(3)','<strong>斯蒂芬·库里</strong>球迷，平时也喜欢打篮球和乒乓球。'],
    ['#contact h2','<span class="section-index">06</span> 联系我'], ['#contact p','欢迎就研究、想法或潜在合作与我交流。'],
    ['.contacts a[href^="mailto:"]','电子邮箱'], ['.contacts a[href$=".pdf"]','下载简历 ↓'], ['.foot','© Jiachi Zhang · 中国广州']
  ];
  const french = {
    '.nav a[href="#about"]': 'À propos', '.nav a[href="#interests"]': 'Recherche', '.nav a[href="#news"]': 'Actualités', '.nav a[href="#research"]': 'Publications', '.nav a[href="#contact"]': 'Contact',
    '.bio': 'IA efficace · compréhension multimodale', '.affiliation strong': 'South China University of Technology', '.affiliation span': 'Guangzhou, Chine',
    '.profile-links a[href^="mailto:"]': 'E-mail', '.profile-links a[href$=".pdf"]': 'Curriculum vitæ',
    '.subtitle': 'Étudiant-chercheur · South China University of Technology',
    '#affiliations h2': 'Institutions',
    '.institution:nth-child(1) h3': 'South China University of Technology', '.institution:nth-child(1) p': 'Licence · ingénierie de l’information',
    '.institution:nth-child(2) h3': 'SIAT, Académie chinoise des sciences', '.institution:nth-child(2) p': 'Stagiaire de recherche invité',
    '.institution:nth-child(3) h3': 'The Chinese University of Hong Kong, Shenzhen', '.institution:nth-child(3) p': 'Stagiaire de recherche invité',
    '#about h2': '<span class="section-index">01</span> À propos',
    '#about p:nth-of-type(1)': 'Je suis étudiant en licence d’ingénierie, spécialité <strong>ingénierie de l’information</strong>, à la <strong>South China University of Technology (SCUT)</strong> (2023–2027).',
    '#about p:nth-of-type(2)': 'Je suis stagiaire de recherche invité au <strong>Shenzhen Institutes of Advanced Technology de l’Académie chinoise des sciences (SIAT, CAS)</strong>, sous la direction de <strong>Wenqi Fang</strong> et du doctorant <strong>Zhuoyu Wu</strong>. Mes travaux portent sur la segmentation légère d’images médicales et le raffinement efficace des prédictions.',
    '#about p:nth-of-type(3)': 'Je suis également stagiaire de recherche invité dans le groupe du professeur <strong>Ming Li à la Chinese University of Hong Kong, Shenzhen</strong>, où je contribue à des recherches sur l’évaluation multimodale des comportements d’enfants autistes.',
    '#about p:nth-of-type(4)': 'Je serais ravi d’échanger sur la recherche, des idées ou de futures collaborations. N’hésitez pas à me contacter par <a href="mailto:jingzhizhang569@gmail.com">e-mail</a> !',
    '#interests h2': '<span class="section-index">02</span> Intérêts de recherche',
    '#interests p:nth-of-type(1)': 'Je souhaite concevoir des <strong>systèmes d’IA interactifs et efficaces</strong> capables de comprendre le monde en continu et d’aider les personnes en temps réel. Une question guide mes recherches : <strong>comment un système d’IA peut-il conserver et actualiser les informations importantes avec des ressources de calcul limitées ?</strong>',
    '#interests p:nth-of-type(2)': 'Mes travaux précédents portent sur les architectures légères et le raffinement des prédictions pour la segmentation d’images médicales. Je souhaite prolonger cette approche vers la <strong>compréhension multimodale en flux continu</strong> : comment maintenir un contexte utile, comprendre les interactions en cours et réagir de manière adaptée dans un environnement dynamique.',
    '#interests p:nth-of-type(3)': 'À plus long terme, j’espère développer des assistants capables d’apprendre à partir de données sensorielles continues et d’aider les personnes au quotidien, en prêtant attention à la <strong>réactivité, à l’efficacité et à la qualité de l’interaction</strong>.',
    '.research-topics span:nth-child(1)': 'IA efficace', '.research-topics span:nth-child(2)': 'Compréhension multimodale en continu', '.research-topics span:nth-child(3)': 'Intelligence interactive',
    '#news h2': '<span class="section-index">03</span> Actualités',
    '.news li:nth-child(1) span': 'Début d’un stage de recherche invité à <strong>CUHK-Shenzhen</strong> sur l’évaluation comportementale multimodale.',
    '.news li:nth-child(2) span': '<strong>Gain-Aware Controller</strong> accepté à <strong>ICONIP 2026</strong>.',
    '.news li:nth-child(3) span': '<strong>RIGS-Refiner</strong> accepté à <strong>APSIPA ASC 2026</strong> pour une <strong>présentation orale</strong>.',
    '.news li:nth-child(4) span': 'Début d’un stage de recherche invité au <strong>SIAT, CAS</strong>, consacré à l’IA médicale ultra-légère.',
    '#research h2': '<span class="section-index">04</span> Travaux sélectionnés',
    '.paper:nth-child(1) h3 a': 'Segmentation légère des polypes par un contrôleur récursif sensible au gain dans l’espace des prédictions',
    '.paper:nth-child(1) p': 'Un module prêt à l’emploi de 189 paramètres affine les prédictions de segmentation en suivant les écarts et l’incertitude. Il apporte des gains constants sur sept architectures sans modifier leur structure.',
    '.paper:nth-child(1) .author': 'Premier auteur', '.paper:nth-child(1) .venue': 'ICONIP 2026 · Accepté',
    '.paper:nth-child(2) h3 a': 'RIGS-Refiner : raffinement récursif guidé par le risque pour la segmentation des polypes en coloscopie',
    '.paper:nth-child(2) p': 'Un module de 519 paramètres utilise les informations issues des prédictions pour effectuer une correction sélective guidée par le risque et surpasse des méthodes de post-traitement plus coûteuses.',
    '.paper:nth-child(2) .author': 'Premier auteur', '.paper:nth-child(2) .venue': 'APSIPA ASC 2026 <b class="oral">ORAL</b>',
    '.paper:nth-child(1) .paperlink': 'Article ↗', '.paper:nth-child(2) .paperlink': 'Article ↗', '.paper:nth-child(1) .figure span': 'Agrandir ↗', '.paper:nth-child(2) .figure span': 'Agrandir ↗',
    '#miscs h2': '<span class="section-index">05</span> En dehors de la recherche',
    '.misc li:nth-child(1)': 'Ancien <strong>président de la troupe artistique de SCUT (EE)</strong>, où j’ai aimé réunir des passionnés de spectacle.',
    '.misc li:nth-child(2)': 'Grand amateur de la musique de <strong>Khalil Fong (方大同)</strong>, j’aime aussi chanter, surtout sous la douche.',
    '.misc li:nth-child(3)': 'Supporter de <strong>Stephen Curry</strong>, je joue régulièrement au basket et au tennis de table.',
    '#contact h2': '<span class="section-index">06</span> Me contacter', '#contact p': 'Je serais ravi d’échanger sur la recherche, des idées ou de futures collaborations.',
    '.contacts a[href^="mailto:"]': 'E-mail', '.contacts a[href$=".pdf"]': 'Télécharger le CV ↓', '.foot': '© Jiachi Zhang · Guangzhou, Chine'
  };
  const entries = translations.map(([selector, zh]) => {
    const element = document.querySelector(selector);
    return element ? { element, en: element.innerHTML, zh, fr: french[selector] || element.innerHTML } : null;
  }).filter(Boolean);
  const buttons = [...document.querySelectorAll('[data-language]')];
  const setLanguage = language => {
    const selected = ['en', 'zh', 'fr'].includes(language) ? language : 'en';
    entries.forEach(entry => { entry.element.innerHTML = entry[selected]; });
    document.documentElement.lang = selected === 'zh' ? 'zh-CN' : selected;
    document.title = selected === 'zh' ? '张伽弛 | 学术主页' : selected === 'fr' ? 'Jiachi Zhang | Page académique' : 'Jiachi Zhang | Academic Homepage';
    document.querySelector('.nav').setAttribute('aria-label', selected === 'zh' ? '主导航' : selected === 'fr' ? 'Navigation principale' : 'Main navigation');
    document.querySelector('.modal').setAttribute('aria-label', selected === 'zh' ? '论文图片' : selected === 'fr' ? 'Figure de recherche' : 'Research figure');
    document.querySelector('.modal-close').setAttribute('aria-label', selected === 'zh' ? '关闭图片' : selected === 'fr' ? 'Fermer la figure' : 'Close figure');
    buttons.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.language === selected)));
    try { localStorage.setItem('homepage-language', selected); } catch (_) {}
  };
  buttons.forEach(button => button.addEventListener('click', () => setLanguage(button.dataset.language)));
  let saved = 'en';
  try { saved = localStorage.getItem('homepage-language') || 'en'; } catch (_) {}
  setLanguage(saved);
})();
