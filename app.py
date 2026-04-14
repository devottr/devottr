from flask import Flask, jsonify, send_from_directory, render_template_string

app = Flask(__name__, static_folder="assets", static_url_path="/assets")

data = {
    "characters": [
        {
            "name": "<span>Daniel</span>",
            "status": "Aspirin' Software Developer",
            "species": "Welcome to my page!",
            "image": "./assets/img.jpg",
            "email": '<a href="mailto:web.relax970@passinbox.com"><svg fill="currentColor" width="16" height="16" viewBox="0 0 1920 1920" xmlns="http://www.w3.org/2000/svg"><path d="M1920 428.266v1189.54l-464.16-580.146-88.203 70.585 468.679 585.904H83.684l468.679-585.904-88.202-70.585L0 1617.805V428.265l959.944 832.441L1920 428.266ZM1919.932 226v52.627l-959.943 832.44L.045 278.628V226h1919.887Z" fill-rule="evenodd"/></svg> Email</a>',
            "telegram": '<a href="https://t.me/made_the_cut" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-telegram" viewBox="0 0 16 16"><path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0M8.287 5.906q-1.168.486-4.666 2.01-.567.225-.595.442c-.03.243.275.339.69.47l.175.055c.408.133.958.288 1.243.294q.39.01.868-.32 3.269-2.206 3.374-2.23c.05-.012.12-.026.166.016s.042.12.037.141c-.03.129-1.227 1.241-1.846 1.817-.193.18-.33.307-.358.336a8 8 0 0 1-.188.186c-.38.366-.664.64.015 1.088.327.216.589.393.85.571.284.194.568.387.936.629q.14.092.27.187c.331.236.63.448.997.414.214-.02.435-.22.547-.82.265-1.417.786-4.486.906-5.751a1.4 1.4 0 0 0-.013-.315.34.34 0 0 0-.114-.217.53.53 0 0 0-.31-.093c-.3.005-.763.166-2.984 1.09"></path></svg> Telegram</a>',
            "whatsApp": '<a href="https://wa.me/2349153417260" target="_blank"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-whatsapp" viewBox="0 0 16 16"><path d="M13.601 2.326A7.85 7.85 0 0 0 7.994 0C3.627 0 .068 3.558.064 7.926c0 1.399.366 2.76 1.057 3.965L0 16l4.204-1.102a7.9 7.9 0 0 0 3.79.965h.004c4.368 0 7.926-3.558 7.93-7.93A7.9 7.9 0 0 0 13.6 2.326zM7.994 14.521a6.6 6.6 0 0 1-3.356-.92l-.24-.144-2.494.654.666-2.433-.156-.251a6.56 6.56 0 0 1-1.007-3.505c0-3.626 2.957-6.584 6.591-6.584a6.56 6.56 0 0 1 4.66 1.931 6.56 6.56 0 0 1 1.928 4.66c-.004 3.639-2.961 6.592-6.592 6.592m3.615-4.934c-.197-.099-1.17-.578-1.353-.646-.182-.065-.315-.099-.445.099-.133.197-.513.646-.627.775-.114.133-.232.148-.43.05-.197-.1-.836-.308-1.592-.985-.59-.525-.985-1.175-1.103-1.372-.114-.198-.011-.304.088-.403.087-.088.197-.232.296-.346.1-.114.133-.198.198-.33.065-.134.034-.248-.015-.347-.05-.099-.445-1.076-.612-1.47-.16-.389-.323-.335-.445-.34-.114-.007-.247-.007-.38-.007a.73.73 0 0 0-.529.247c-.182.198-.691.677-.691 1.654s.71 1.916.81 2.049c.098.133 1.394 2.132 3.383 2.992.47.205.84.326 1.129.418.475.152.904.129 1.246.08.38-.058 1.171-.48 1.338-.943.164-.464.164-.86.114-.943-.049-.084-.182-.133-.38-.232"></path></svg> WhatsApp</a>'
        }
    ]
}

INDEX_HTML = """
<!DOCTYPE html><html lang="en"><head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta charset="UTF-8">
    <title>My page</title>
    <meta name="description" content="My page">
  <meta name="keywords" content="Daniel's page">
  <meta name="author" content="Daniel A">
<link rel="icon" href="/assets/favicon.ico">
  <link href="/assets/styles.css" rel="stylesheet">
<style>
h1, span{
  --c1: #9ccce8;
  --c2: #2e88c7;
  
  --_p: 93% 83.5% at;
  --_g1: radial-gradient(var(--_p) bottom,var(--c1) 79.5%,#0000 80%) no-repeat;
  --_g2: radial-gradient(var(--_p) top   ,#0000 79.5%,var(--c1) 80%) no-repeat;
  --_g3: radial-gradient(var(--_p) bottom,var(--c2) 79.5%,#0000 80%) no-repeat;
  --_g4: radial-gradient(var(--_p) top   ,#0000 79.5%,var(--c2) 80%) no-repeat;
  background: 
    var(--_g1),var(--_g2),var(--_g1),var(--_g2),
    var(--_g3),var(--_g4),var(--_g3),var(--_g4);
  -webkit-background-clip: text;
          background-clip: text;
  color: #0000;
  -webkit-text-stroke: 0.1rem var(--c1);
  -webkit-box-decoration-break: clone;
          box-decoration-break: clone;
  animation: 
    s 2s infinite alternate,
    m 3s infinite linear;
}
@keyframes m {
  0% {background-position:
    -200% 100%,-100% 100%,  0% 100%,100% 100%,
       0% 100%, 100% 100%,200% 100%,300% 100%}
  100%{background-position:   
        0% 100%, 100% 100%,200% 100%,300% 100%,
     -200% 100%,-100% 100%,  0% 100%,100% 100%}
}
@keyframes s{
  0%  {background-size:
        50.5% 60%, 50.5% 60%, 50.5% 60%, 50.5% 60%,
        50.5% 90%, 50.5% 90%, 50.5% 90%, 50.5% 90%}
  33% {background-size: 
        50.5% 70%, 50.5% 70%, 50.5% 70%, 50.5% 70%,
        50.5% 75%, 50.5% 75%, 50.5% 75%, 50.5% 75%}
  66% {background-size: 
        50.5% 55%, 50.5% 55%, 50.5% 55%, 50.5% 55%,
        50.5% 80%, 50.5% 80%, 50.5% 80%, 50.5% 80%}
  100%{background-size: 
        50.5% 90%, 50.5% 90%, 50.5% 90%, 50.5% 90%,
        50.5% 95%, 50.5% 95%, 50.5% 95%, 50.5% 95%}
}
a {
  --s: .25em; /* control the wave*/

  padding: .4em .5em;
  background-color: #BF4D28;
  color: #fff;
  --_s: calc(var(--s)*4) 51% repeat-x;
  --_r: calc(1.345*var(--s)) at left 50%;
  --_g1: #000 99%,#0000 101%;
  --_g2: #0000 99%,#000 101%;
  --mask:
    radial-gradient(var(--_r) top    calc(var(--s)* 1.9),var(--_g1))
     calc(50% - 2*var(--s) - var(--_i,0px)) 0/var(--_s),
    radial-gradient(var(--_r) top    calc(var(--s)*-0.9),var(--_g2))
     calc(50% - var(--_i,0px)) var(--s)/var(--_s),
    radial-gradient(var(--_r) bottom calc(var(--s)* 1.9),var(--_g1))
     calc(50% - 2*var(--s) + var(--_i,0px)) 100%/var(--_s),
    radial-gradient(var(--_r) bottom calc(var(--s)*-0.9),var(--_g2))
     calc(50% + var(--_i,0px)) calc(100% - var(--s))/var(--_s);
  -webkit-mask: var(--mask);
          mask: var(--mask);
  cursor: pointer;
}
a:hover {
  --_i: calc(4*var(--s));
  transition: .35s;
}
a:active {
  background-image: linear-gradient(#0004 0 0);
}
a:focus-visible {
  -webkit-mask: none;
  outline-offset: .1em;
  padding: .2em .5em;
  margin: .2em 0;
}
img {
height: 200px;
  width: 200px;
  border-radius: 100px;
  object-fit: cover;
  animation: bounce 2s;
}
h1 {
  font-size: 3rem;
}

body {
 background: linear-gradient(green, darkgreen);
  color: white;
  font-family: 'Trebuchet MS';
  text-align: center;
  height: 100%;
}
div {
    display: flex;
    flex-flow: column nowrap;
    justify-content: center;
  align-items: center;
margin: 2.5vh;
}
a {
  background-color: white;
  font-size: 20px;
  border-radius:50vw;
  padding: 15px;
  display: block;
  text-align: center;
  margin: 1px;
  color: green;
  text-decoration: none;
}
@keyframes bounce {
    0%, 20%, 50%, 80%, 100% { 
        transform: translateY(0);
    }
    40% {
        transform: translateY(-30px);
    }
    60% {
        transform: translateY(-15px);
    }
}

@keyframes gradient {
    0% {
        background-position: 0% 50%;
    }
    50% {
        background-position: 100% 50%;
    }
    100% {
        background-position: 0% 50%;
    }
}</style>
 </head>
<body>
  <div id="root"></div>
  <script>
    fetch('/api/characters').then(r=>r.json()).then(data=>{
      const character = data.characters[0];
      const root = document.getElementById('root');

      const img = document.createElement('img');
      img.src = character.image;
      img.alt = character.name;
      img.className = 'character-image';
      root.appendChild(img);

      const name = document.createElement('h1');
      name.className = 'character-detail';
      name.innerHTML = character.name;
      root.appendChild(name);

      const status = document.createElement('h2');
      status.className = 'character-detail';
      status.innerHTML = character.status;
      root.appendChild(status);

      const species = document.createElement('p');
      species.className = 'character-detail';
      species.innerHTML = character.species;
      root.appendChild(species);

      const email = document.createElement('div');
      email.className = 'character-detail';
      email.innerHTML = character.email;
      root.appendChild(email);

      const telegram = document.createElement('div');
      telegram.className = 'character-detail';
      telegram.innerHTML = character.telegram;
      root.appendChild(telegram);

      const whatsapp = document.createElement('div');
      whatsapp.className = 'character-detail';
      whatsapp.innerHTML = character.whatsApp;
      root.appendChild(whatsapp);
    });
  </script>
  <noscript><h1>Please enable JavaScript!</h1></noscript>
</body>
</html>
"""

@app.route("/api/characters")
def get_characters():
    return jsonify(data)

@app.route("/")
def index():
    return render_template_string(INDEX_HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

