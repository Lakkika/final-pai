import os
import glob

css = """    <style>
        .vertical-divider { border-left: 1px solid #C5D6C0; height: 100%; }
        @keyframes float { 0% { transform: translateY(0px); } 50% { transform: translateY(-10px); } 100% { transform: translateY(0px); } }
        .float-3d { animation: float 6s ease-in-out infinite; }
        @keyframes float-slow { 0% { transform: translateY(0px) rotate(0deg); } 50% { transform: translateY(-15px) rotate(2deg); } 100% { transform: translateY(0px) rotate(0deg); } }
        .float-3d-slow { animation: float-slow 8s ease-in-out infinite; }
        .glass-card-3d {
            background: rgba(255, 255, 255, 0.7);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.8);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.08), inset 0 1px 0 rgba(255,255,255,1);
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }
        .glass-card-3d:hover {
            transform: translateY(-8px) scale(1.02);
            box-shadow: 0 30px 60px rgba(107, 157, 69, 0.15), inset 0 1px 0 rgba(255,255,255,1);
        }
        .bg-blob { position: fixed; border-radius: 50%; filter: blur(80px); z-index: -1; opacity: 0.5; }
    </style>"""

blobs = """<body class="font-sans text-gray-800 bg-gradient-to-br from-[#F4F9F4] via-[#FFFFFF] to-[#E9F4E9] bg-fixed flex flex-col min-h-screen relative">
    <div class="bg-blob w-[500px] h-[500px] bg-primary/20 top-[-10%] left-[-10%] float-3d-slow pointer-events-none"></div>
    <div class="bg-blob w-[600px] h-[600px] bg-[#a8e0a8]/30 bottom-[-20%] right-[-10%] float-3d pointer-events-none"></div>"""

files = glob.glob(r'c:\\laragon\\www\\final pai\\*.html')

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update CSS
    if '<style>' in content and '</style>' in content:
        start = content.find('<style>')
        end = content.find('</style>') + 8
        content = content[:start] + css + content[end:]
    else:
        # If no style tag exists, insert it before </head>
        head_end = content.find('</head>')
        if head_end != -1:
            content = content[:head_end] + css + '\n' + content[head_end:]

    # 2. Add Background Blobs
    body_tag = '<body class="font-sans text-gray-800 bg-gradient-to-br from-[#F4F9F4] via-[#FFFFFF] to-[#E9F4E9] bg-fixed flex flex-col min-h-screen">'
    if body_tag in content:
        content = content.replace(body_tag, blobs)
        
    # 3. Replace Cards with Glass-card-3d
    # menu.html & index.html cards
    content = content.replace('bg-white rounded-2xl p-4 shadow-[0_8px_30px_rgb(0,0,0,0.06)] hover:shadow-[0_20px_40px_rgb(0,0,0,0.12)] transform hover:-translate-y-2 transition-all duration-300', 'glass-card-3d rounded-2xl p-4')
    # index.html banners
    content = content.replace('relative bg-white rounded-2xl overflow-hidden flex h-48 md:h-56 shadow-[0_15px_40px_rgba(0,0,0,0.08)] hover:shadow-[0_25px_50px_rgba(107,157,69,0.2)] transform hover:-translate-y-2 transition-all duration-500 group border border-gray-100', 'relative glass-card-3d rounded-2xl overflow-hidden flex h-48 md:h-56 group border-none')
    content = content.replace('relative bg-white rounded-2xl overflow-hidden flex h-48 md:h-56 shadow-[0_15px_40px_rgba(0,0,0,0.08)] hover:shadow-[0_25px_50px_rgba(0,0,0,0.15)] transform hover:-translate-y-2 transition-all duration-500 group border border-gray-100', 'relative glass-card-3d rounded-2xl overflow-hidden flex h-48 md:h-56 group border-none')
    # about.html
    content = content.replace('bg-white rounded-2xl p-8 flex flex-col items-center text-center shadow-[0_10px_30px_rgba(0,0,0,0.05)] border border-gray-100 hover:shadow-[0_20px_40px_rgba(107,157,69,0.15)] transform hover:-translate-y-2 transition-all duration-300', 'glass-card-3d rounded-2xl p-8 flex flex-col items-center text-center')
    content = content.replace('bg-white rounded-3xl overflow-hidden relative flex flex-col md:flex-row items-center min-h-[400px] shadow-[0_20px_50px_rgba(0,0,0,0.08)] border border-gray-50', 'glass-card-3d rounded-3xl overflow-hidden relative flex flex-col md:flex-row items-center min-h-[400px]')
    # contact.html
    content = content.replace('bg-white rounded-3xl shadow-[0_20px_50px_rgba(0,0,0,0.08)] border border-gray-100 p-8 md:p-12 hover:shadow-[0_25px_60px_rgba(107,157,69,0.15)] transition-shadow duration-500', 'glass-card-3d rounded-3xl p-8 md:p-12')
    content = content.replace('bg-white rounded-3xl shadow-[0_20px_50px_rgba(0,0,0,0.08)] border border-gray-100 p-8 md:p-12 flex flex-col hover:shadow-[0_25px_60px_rgba(0,0,0,0.12)] transition-shadow duration-500 relative overflow-hidden', 'glass-card-3d rounded-3xl p-8 md:p-12 flex flex-col relative overflow-hidden')
    # article.html
    content = content.replace('bg-white p-8 rounded-2xl shadow-[0_10px_30px_rgba(0,0,0,0.05)] border border-gray-50 hover:shadow-[0_15px_40px_rgba(0,0,0,0.08)] transition-shadow', 'glass-card-3d p-8 rounded-2xl')
    content = content.replace('bg-white rounded-2xl p-8 shadow-[0_10px_30px_rgba(0,0,0,0.05)] border border-gray-100', 'glass-card-3d rounded-2xl p-8')
    content = content.replace('bg-white rounded-2xl overflow-hidden relative flex flex-col md:flex-row items-center min-h-[350px] shadow-[0_15px_40px_rgba(0,0,0,0.08)] hover:shadow-[0_20px_50px_rgba(107,157,69,0.15)] transition-shadow duration-500 border border-gray-50', 'glass-card-3d rounded-2xl overflow-hidden relative flex flex-col md:flex-row items-center min-h-[350px]')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated all files with 3D aesthetic.")
