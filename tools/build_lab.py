"""Writes the Codelions Games Lab into ~/git-services/overcodelions-games."""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OVERCLI = 'https://overcodelions.com/overcli/'
CLI = '<svg width="{s}" height="{s}" viewBox="0 0 32 32" fill="none" stroke="#0d0f15" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 9 L16 16 L9 23"/><path d="M18 23 H24"/></svg>'
LAB = '<svg width="16" height="16" viewBox="0 0 32 32" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 9 L16 16 L9 23"/><circle cx="22.5" cy="22" r="2.6" fill="#ffd25c" stroke="none"/></svg>'
GAMES = [('crater', 'Crater', '#ff8a3d'), ('puttnik', 'Puttnik', '#67e4f7'), ('glidegang', 'Glidegang', '#f8b53f')]
ICON = {'crater': 'crater-icon.png','puttnik': 'puttnik-icon.png', 'glidegang': 'glidegang-icon.png'}


def built(up):
    return f'<a class="built" href="{OVERCLI}" target="_blank" rel="noopener"><span class="mk">{CLI.format(s=16)}</span>Built with <b>overcli</b></a>'


# ── live scenes ─────────────────────────────────────────────────────────
def scene_puttnik():
    stars = ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" opacity="{o}"/>' for x, y, r, o in
                    [(40, 40, 1.4, .9), (120, 90, 1, .6), (210, 30, 1.2, .8), (260, 110, .9, .5), (420, 40, 1.3, .9), (470, 150, 1, .6), (610, 30, 1, .7), (600, 300, 1.2, .6), (380, 320, 1, .5), (250, 300, .9, .5), (180, 200, 1.1, .7), (520, 300, 1, .5)])
    P = 'M 92 250 C 150 70, 300 46, 352 140 S 520 250, 548 197'
    return f'''<svg viewBox="0 0 640 360" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
<defs><radialGradient id="pb" cx="25%" cy="20%" r="95%"><stop offset="0" stop-color="#3a2f96"/><stop offset=".55" stop-color="#151140"/><stop offset="1" stop-color="#0a2f3e"/></radialGradient>
<radialGradient id="pg" cx="35%" cy="30%" r="75%"><stop offset="0" stop-color="#b8f58a"/><stop offset=".6" stop-color="#5fbf5a"/><stop offset="1" stop-color="#2f7d4a"/></radialGradient>
<radialGradient id="pt" cx="35%" cy="30%" r="75%"><stop offset="0" stop-color="#9ff0d8"/><stop offset=".6" stop-color="#3fae9a"/><stop offset="1" stop-color="#1f6a68"/></radialGradient>
<radialGradient id="pm" cx="35%" cy="30%" r="70%"><stop offset="0" stop-color="#fff"/><stop offset="1" stop-color="#a9b0c6"/></radialGradient>
<radialGradient id="ph" r=".5"><stop offset="0" stop-color="#67e4f7" stop-opacity=".55"/><stop offset="1" stop-color="#67e4f7" stop-opacity="0"/></radialGradient>
<radialGradient id="po" cx="35%" cy="30%" r="70%"><stop offset="0" stop-color="#ffd2a1"/><stop offset="1" stop-color="#c7743f"/></radialGradient></defs>
<rect width="640" height="360" fill="url(#pb)"/>{stars}
<g transform="translate(560 64)"><circle r="22" fill="url(#po)"/><ellipse rx="40" ry="9" fill="none" stroke="#f1c48c" stroke-width="4" transform="rotate(-14)"/></g>
<circle class="p-glow" cx="330" cy="150" r="70" fill="url(#ph)"/>
<circle cx="330" cy="150" r="30" fill="url(#pm)"/>
<path class="p-trail" d="{P}" fill="none" stroke="#67e4f7" stroke-width="2.5" stroke-linecap="round" opacity=".7"/>
<circle cx="92" cy="322" r="74" fill="url(#pg)"/><ellipse cx="70" cy="300" rx="16" ry="9" fill="#3f9a52" opacity=".5"/><ellipse cx="118" cy="330" rx="20" ry="10" fill="#3f9a52" opacity=".45"/>
<circle cx="560" cy="252" r="56" fill="url(#pt)"/><ellipse cx="548" cy="199" rx="16" ry="6" fill="#c8f7a6" opacity=".7"/><ellipse cx="548" cy="199" rx="7" ry="3.2" fill="#08111a"/>
<line x1="551" y1="198" x2="556" y2="152" stroke="#f2f4ff" stroke-width="2.6" stroke-linecap="round"/><path class="p-flag" d="M556 152 L580 160 L554 170 Z" fill="#ff5d6a"/>
<g><circle r="13" fill="#67e4f7" opacity=".3"/><circle r="6.5" fill="#fff"/>
<animateMotion dur="5.2s" repeatCount="indefinite" path="{P}" keyPoints="0;0;1;1" keyTimes="0;.08;.82;1" calcMode="spline" keySplines="0 0 1 1;.45 .05 .35 1;0 0 1 1"/>
<animate attributeName="opacity" dur="5.2s" repeatCount="indefinite" values="0;1;1;0;0" keyTimes="0;.08;.82;.9;1"/></g>
</svg>'''


def ridge(points, color, extra=''):
    pts = ' '.join(f'L{x} {y}' for x, y in points)
    d = f'M0 360 {pts} L640 360 Z'
    return f'<path d="{d}" fill="{color}"{extra}/><path d="{d}" fill="{color}" transform="translate(640 0)"{extra}/>'


def scene_glidegang():
    far = ridge([(0, 236), (60, 214), (110, 232), (170, 196), (230, 216), (300, 186), (360, 210), (420, 192), (480, 224), (540, 202), (600, 226), (640, 236)], '#d9945e', ' opacity=".75"')
    mid = ridge([(0, 268), (70, 250), (120, 266), (190, 232), (250, 258), (320, 244), (380, 270), (440, 240), (500, 262), (570, 250), (640, 268)], '#c26a3c')
    near = ridge([(0, 306), (50, 290), (100, 304), (160, 272), (210, 296), (270, 282), (330, 310), (390, 276), (450, 300), (510, 288), (580, 306), (640, 306)], '#93391f')
    G = 'M -40 120 C 120 60, 220 220, 330 168 S 520 70, 700 140'
    rings = ''.join(f'<g transform="translate({x} {y}) rotate({r})"><ellipse class="g-ring" rx="15" ry="27" fill="none" stroke="#f8b53f" stroke-width="6"/><ellipse rx="15" ry="27" fill="none" stroke="#a3561c" stroke-width="1.5" opacity=".6"/></g>' for x, y, r in [(150, 118, -12), (330, 168, 8), (540, 100, -6)])
    thermals = ''.join(f'<g class="g-thermal" style="animation-delay:{d}s"><path d="M{x} 300 q -6 -20 0 -40 q 6 -20 0 -40" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" opacity=".5"/></g>' for x, d in [(246, 0), (262, .9), (430, .4), (446, 1.5)])
    streaks = ''.join(f'<line class="g-streak" x1="640" y1="{y}" x2="0" y2="{y}" stroke="#fff" stroke-width="1.4" opacity=".35" style="animation-delay:{d}s"/>' for y, d in [(70, 0), (150, .5), (205, .2), (110, .9)])
    return f'''<svg viewBox="0 0 640 360" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
<defs><linearGradient id="gs" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1d4fbd"/><stop offset=".55" stop-color="#58a6ee"/><stop offset=".8" stop-color="#f6d6a2"/><stop offset="1" stop-color="#f0a66a"/></linearGradient>
<radialGradient id="gu" r=".5"><stop offset="0" stop-color="#fff4cf"/><stop offset=".45" stop-color="#ffe2a0" stop-opacity=".8"/><stop offset="1" stop-color="#ffe2a0" stop-opacity="0"/></radialGradient></defs>
<rect width="640" height="360" fill="url(#gs)"/><circle cx="500" cy="84" r="80" fill="url(#gu)"/>{streaks}
<g class="g-far">{far}</g>{thermals}<g class="g-far" style="animation-duration:26s">{mid}</g>{rings}
<g><g transform="scale(2)"><path d="M20 0 L-14 -13 L-8 0 L-14 13 Z" fill="#fff"/><path d="M8 -4.2 L-9 -10.5 L-11 -7.5 Z M8 4.2 L-9 10.5 L-11 7.5 Z" fill="#2f86e2"/><path d="M-8 0 L-14 -13 L-14 13 Z" fill="#e3e6ee"/><circle cx="-2" cy="0" r="3" fill="#1b2a4e"/><circle cx="-2" cy="0" r="1.4" fill="#f8b53f"/></g>
<animateMotion dur="4.6s" repeatCount="indefinite" rotate="auto" path="{G}"/></g>
<g class="g-near">{near}</g></svg>'''


def scene_crater():
    return '<img class="cover still" src="{up}assets/crater-play.jpg" alt="Crater on an iPhone: a desert island, 2:32 left, aiming a Rain shot at 73 degrees across the water" />'


def scene_puttnik_shot():
    return '<img class="cover still" src="{up}assets/puttnik-play.jpg" alt="Puttnik on an iPhone: Moonfield, hole 5, Little Moon — aiming a shot around a moon to the cup" />'


def scene_glidegang_shot():
    return '<img class="cover still" src="{up}assets/glidegang-vents.jpg" alt="Glidegang on an iPhone: Volcano Vents, gliding over a lava river toward the next gate" />'


SCENES = {'crater': scene_crater, 'puttnik': scene_puttnik_shot, 'glidegang': scene_glidegang_shot}


def scene(game, up):
    return f'<span class="scene">{SCENES[game]().replace("{up}", up)}</span>'


STATUS = '<p class="status"><span class="live"><i></i>Testing now</span><span>on our own iPhones · TestFlight next · then the App Store</span></p>'

# ── page frame ──────────────────────────────────────────────────────────
def page(path, title, desc, cls, current, body):
    up = '../' if path else ''
    links = [('', 'Lab', None)] + [(f'{g}/', n, c) for g, n, c in GAMES] + [('how-we-build/', 'How we build', None)]
    nav = ''.join(f'<a href="{up}{h}"' + (' aria-current="page"' if h == current else '') + '>' + (f'<i class="dot" style="background:{c}"></i>' if c else '') + f'{n}</a>' for h, n, c in links)
    html = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <meta property="og:type" content="website" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{desc}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500..800&family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="{up}lab.css" />
</head>
<body class="{cls}">
  <header class="nav"><div class="wrap">
    <a class="brand" href="{up}" aria-label="codelions games lab"><span class="brand-mark"><span>{LAB}</span></span><b>codelions</b><i>games lab</i></a>
    <nav class="nav-links" aria-label="games">{nav}</nav>
    <span class="nav-right">{built(up)}</span>
  </div></header>
  <main>
{body}
  </main>
  <footer class="foot"><div class="wrap">
    <span><b style="font-family: 'Bricolage Grotesque'; font-size: 15px; color: var(--ink)">codelions games lab</b> · made by <a href="https://github.com/lionelfarr" target="_blank" rel="noopener">Lionel</a> &amp; <a href="https://github.com/owenlfarr" target="_blank" rel="noopener">Owen</a> Farr</span>
    <span>{built(up)}<a href="https://overcodelions.com/" target="_blank" rel="noopener">our dev tools ↗</a></span>
  </div></footer>
</body>
</html>
'''
    full = os.path.join(ROOT, path, 'index.html')
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, 'w').write(html)


def chips(items, lab=False):
    s = ''.join(f'<span class="chip"><i></i>{c}</span>' for c in items)
    if lab:
        s += '<span class="chip lab"><i></i>testing now · coming soon to the App Store</span>'
    return f'<div class="chips">{s}</div>'


def feats(items):
    return '<div class="feats">' + ''.join(f'<div class="feat"><span class="n">{i + 1:02d}</span><b>{t}</b><p>{d}</p></div>' for i, (t, d) in enumerate(items)) + '</div>'


def strip(items):
    return '<div class="strip">' + ''.join(f'<div><b>{a}</b><p>{b}</p></div>' for a, b in items) + '</div>'


def lst(rows):
    return '<div class="list">' + ''.join(f'<div><b>{a}</b><span>{b}</span></div>' for a, b in rows) + '</div>'


def band(up, text):
    return f'''    <section class="sec"><div class="wrap">
      <div class="band"><div class="t"><span class="bmark">{CLI.format(s=30)}</span><h3>Built with overcli.</h3><p class="body" style="max-width: 640px">{text}</p></div>
      <div class="btns"><a class="btn btn-ink" href="{OVERCLI}" target="_blank" rel="noopener">Meet overcli ↗</a><a class="btn btn-line" href="{up}how-we-build/">How we build</a></div></div>
    </div></section>'''


def game_hero(game, up, eyebrow, h1, lede, chip_items, note):
    return f'''    <section class="hero"><div class="wrap">
      <div class="hero-copy"><p class="eyebrow">[ <b>{game}</b> ] · {eyebrow}</p>{STATUS}<h1>{h1}</h1><p class="lede">{lede}</p>{chips(chip_items)}
        <div class="btns"><a class="btn btn-ink" href="#how">How it plays ↓</a><a class="btn btn-line" href="{up}">All the games</a></div></div>
      <div><div class="phone">{scene(game, up)}</div><p class="meta shot-note">{note}</p></div>
    </div></section>'''


# ── the lab ─────────────────────────────────────────────────────────────
fan = ''.join(f'<a class="{g}" href="{g}/">{scene(g, "")}<span class="tag">{n}</span><span class="live badge sm"><i></i>Testing</span></a>' for g, n, c in GAMES)
cards = ''
blurbs = {
    'crater': ('Artillery · 1–4 players', 'Real-time tanks on an island split by mountains. Lob shells over the ridges, or blast straight through them: every hit reshapes the ground.'),
    'puttnik': ('Mini golf · 1–8 players', 'Flick a glowing ball off a planet and let gravity take over. It curves around moons, slingshots past gas giants and skims black holes.'),
    'glidegang': ('Glider racing · 8 racers', 'Eight pilots dive off a cliff through canyons and sea stacks, ride updrafts, steal slipstreams and bump each other into rock walls.')}
for g, n, c in GAMES:
    icon = f'<img src="assets/{ICON[g]}" alt="" />' if ICON[g] else '<span class="ph"></span>'
    kind, text = blurbs[g]
    cards += f'<a class="card {g}" href="{g}/"><span class="pic">{scene(g, "")}<span class="live badge"><i></i>Testing now</span></span><span class="card-body"><span class="card-top">{icon}<span><span class="meta">{kind}</span><h3>{n}</h3></span></span><p>{text}</p><span class="card-foot"><span class="chip lab"><i></i>coming soon to the App Store</span><span class="go">Look inside →</span></span></span></a>'
now = [('crater', 'Crater', 'Playable: random themed islands, four modes, a shop, and same-Wi-Fi multiplayer.', 'next · <b>online play on Game Center</b>'),
       ('puttnik', 'Puttnik', 'Four worlds, journey holes, a live hole clock, clubs and Quick Match are in.', 'next · <b>online play on Game Center</b>'),
       ('glidegang', 'Glidegang', 'All twelve milestones built in one session, with 60 tests passing — and now racing on a real iPhone.', 'next · <b>Party on Wi-Fi, then online</b>')]
board = ''.join(f'<a class="{g}" href="{g}/"><span class="who">' + (f'<img src="assets/{ICON[g]}" alt="" />' if ICON[g] else '<span class="ph"></span>') + f'{n}<span class="live sm"><i></i>Testing</span></span><span class="now">{t}</span><span class="next">{x}</span><span class="arr">→</span></a>' for g, n, t, x in now)
home = f'''    <section class="hero"><div class="wrap">
      <div class="hero-copy"><p class="eyebrow">[ <b>games lab</b> ] · a father and son, making games</p>
        {STATUS}<h1>Small games,<br><em>big physics.</em></h1>
        <p class="lede">Three iPhone games we’re building together, from the first spec to the App Store. Every shot, putt and dive runs on physics we wrote ourselves — so a good player reads the world instead of just reacting to it.</p>
        <div class="btns"><a class="btn btn-ink" href="#games">Meet the games ↓</a><a class="btn btn-line" href="how-we-build/">How we build</a></div>
        {chips(['iPhone · landscape', 'play together', 'built with overcli'])}</div>
      <div class="fan">{fan}</div>
    </div></section>
    <section class="sec" id="games"><div class="wrap">
      <div class="head"><div><p class="eyebrow">[ <b>the games</b> ] · three in the lab</p><h2>Three games, <em>one family.</em></h2></div><p class="lede">They share an engine setup, conventions and code, so each new game starts from what the last one learned.</p></div>
      <div class="games">{cards}</div>
    </div></section>
    <section class="sec"><div class="wrap">
      <div class="head"><div><p class="eyebrow">[ <b>in the lab</b> ] · where each one is</p><h2>Built in the open, <em>one milestone at a time.</em></h2></div><p class="lede">We’re testing all three on our own iPhones now, with TestFlight next and then the App Store. Here’s where each one stands, straight from the repo.</p></div>
      <div class="board">{board}</div>
    </div></section>
    <section class="sec"><div class="wrap">
      <div class="head"><div><p class="eyebrow">[ <b>what they share</b> ]</p><h2>Physics first.</h2></div><p class="lede">No off-the-shelf physics engine in any of them: each game’s world runs on rules we wrote, tuned until it feels right.</p></div>
      {feats([('The world reacts', 'In Crater the ground is the weapon: craters work on any slope, ridges become passes, and steep ground slides away.'),
              ('The same on every phone', 'Puttnik runs each shot 240 times a second from the tee, the flick and the hole’s seed — so a shot replays exactly, anywhere.'),
              ('Air you can read', 'Glidegang flies on its own energy model: diving buys speed, climbing spends it, and updrafts are the only free height.'),
              ('Make your own', 'Puttnik’s Hole Lab and Glidegang’s Course Lab: build it, beat it at par or with a bot, then share it as a code or QR.'),
              ('Play together', 'Game Center online, pass-and-play on one phone, or a whole room on the same Wi-Fi.'),
              ('Bots that play fair', 'Easy, Normal and Hard bots, tuned against a stand-in new player so a first race is winnable and a hard one isn’t.')])}
    </div></section>
{band('', 'Every game here is built with overcli flows, in the agent desktop app we make: one model plans each milestone, another builds it, and a third checks it with Unity’s own tests before we ever pick up a phone.')}
'''
page('', 'Codelions Games Lab — small games, big physics', 'Crater, Puttnik and Glidegang: three iPhone games a father and son are building. Built with overcli.', '', '', home)

# ── Crater ──────────────────────────────────────────────────────────────
crater = f'''{game_hero('crater', '../', 'real-time artillery', 'Every shot <em>reshapes the island.</em>', 'Tanks sit on a big island split by mountains. Lob shells high over the ridges or blast straight through them — every hit changes the ground, and the ground fights back.', ['iPhone · landscape', '1–4 players', 'real time'], 'on an iPhone · a desert island, Rain loaded, 2:32 left')}
    <section class="sec" style="padding-block: 0 clamp(64px, 8vw, 112px); border: 0"><div class="wrap">{strip([('4', 'players, on one island'), ('85°', 'barrels, for lobs behind a mountain'), ('4', 'shells, each with its own reload'), ('3–5 min', 'a match')])}</div></section>
    <section class="sec" id="how"><div class="wrap">
      <div class="head"><div><p class="eyebrow">[ <b>how it plays</b> ]</p><h2>A physics puzzle <em>on a reload timer.</em></h2></div><p class="lede">Real time, not turn-based: everyone fires the moment their weapon has reloaded.</p></div>
      {feats([('Read the shot', 'Angle, direction, power, wind and terrain all matter. Drop a near-vertical lob straight down behind a ridge.'), ('The world is the weapon', 'Hit a ridge enough times and you cut a pass. Steep ground slides away, and the tanks on it fall.'), ('Speed or power', 'Each weapon has its own reload, so you’re always choosing between firing fast and hitting hard.'),
              ('Water fights back', 'Big shells that land in the sea send out a wave ring that shoves tanks near the shore.'), ('Day, sunset, night', 'Three looks for the same island. At night, explosions light it up.'), ('Four modes', 'Classic, Rising Tide, 2v2 and Siege — against bots offline, or with friends on the same Wi-Fi, who join with a 4-letter code.')])}
    </div></section>
    <section class="sec"><div class="wrap">
      <div class="shots"><figure><img src="../assets/crater-fort.jpg" alt="A desert island at the start of a match: full health, a fort on the ridge and the other tank 530 metres away" /><figcaption>desert island · a fort on the ridge, p2 at 530 m</figcaption></figure><figure><img src="../assets/crater-menu.jpg" alt="The Crater menu: Play vs Computer with Classic, Rising Tide, 2v2 and Siege, a Daily Island, time of day, and Play Online on the same Wi-Fi" /><figcaption>the menu · four modes, daily island, same-wi-fi play</figcaption></figure></div>
      <p class="meta" style="margin-top: 18px">Screenshots from an iPhone, from the current build.</p>
    </div></section>
    <section class="sec"><div class="wrap row">
      <div><p class="eyebrow">[ <b>the arsenal</b> ]</p><h2>Four shells, <em>four tactics.</em></h2><p class="body">One of them does no damage at all — it builds a wall.</p></div>
      {lst([('Basic shell', '4 s reload · 20 damage · a small crater'), ('Big shell', '8 s reload · 45 damage · a large crater and a big wave'), ('Splitter', '6 s reload · 3 × 15 damage · three small craters'), ('Dirt bomb', '5 s reload · no damage · adds a mound: block, bury, build a wall')])}
    </div></section>
{band('../', 'Crater came first: its island, terrain and cameras became the starting point for every game after it — and it’s being built the same way, with overcli.')}
'''
page('crater', 'Crater — every shot reshapes the island', 'Real-time 3D artillery for iPhone, for up to 4 players. Every hit reshapes the ground. Built with overcli.', 'crater', 'crater/', crater)

# ── Puttnik ─────────────────────────────────────────────────────────────
puttnik = f'''{game_hero('puttnik', '../', 'mini golf in space', 'Mini golf <em>across tiny planets.</em>', 'Flick a glowing ball off a planet and let gravity take over. It curves around moons, slingshots past gas giants and skims black holes — and if you read the sky right, it drops into the cup on a distant world.', ['iPhone · landscape', '1–8 players', '90 holes'], 'on an iPhone · Moonfield, hole 5 — Little Moon')}
    <section class="sec" style="padding-block: 0 clamp(64px, 8vw, 112px); border: 0"><div class="wrap">{strip([('90', 'holes across 10 worlds'), ('8', 'players online, each in their own time'), ('240', 'physics steps a second'), ('1', 'new hole every day')])}</div></section>
    <section class="sec" style="padding-top: 0; border: 0"><div class="wrap">
      <div class="shots"><figure><img src="../assets/puttnik-stones.jpg" alt="Moonfield, hole 8: Stepping Stones — four small planets to the cup" /><figcaption>moonfield · hole 8 · stepping stones</figcaption></figure><figure><img src="../assets/puttnik-menu.jpg" alt="The Puttnik menu: Play, Daily Hole, Ace Challenge, Play Online, Friends" /><figcaption>the menu · daily hole, ace challenge, play online, friends</figcaption></figure></div>
      <p class="meta" style="margin-top: 18px">Screenshots from an iPhone, from the current build.</p>
    </div></section>
    <section class="sec" id="how"><div class="wrap">
      <div class="head"><div><p class="eyebrow">[ <b>ways to play</b> ]</p><h2>Every hole is <em>a short physics puzzle.</em></h2></div><p class="lede">A shot replays exactly on any phone: the ball runs on our own physics, from the tee, the flick and the hole’s seed.</p></div>
      {feats([('Campaign', 'Ten worlds of nine holes. Stars unlock the next world.'), ('Daily Hole', 'One hole a day, with a Game Center leaderboard.'), ('Pass and Play', '1–4 players on one phone, with a scorecard between holes.'),
              ('Friends', '2–8 players online, each playing the same course in their own time.'), ('Ghost Race', '2–4 players in real time, with the other balls shown as ghosts.'), ('Hole Lab', 'Build your own holes and share them as a code or QR — once you’ve beaten them at par.')])}
    </div></section>
    <section class="sec"><div class="wrap row">
      <div><p class="eyebrow">[ <b>ten worlds</b> ]</p><h2>Each one adds <em>a new idea.</em></h2><p class="body">From gentle gravity curves to the Grand Tour, where everything comes back at once.</p></div>
      {lst([('<i>01</i>Moonfield', 'Gravity curves, rolling on planets, sand'), ('<i>02</i>Ringworks', 'Gas giant atmospheres, boost rings, bumpers'), ('<i>03</i>Frostbelt', 'Ice, asteroid belts, comets'), ('<i>04</i>Black Hole Bay', 'Black holes, wormholes, zero-G zones'), ('<i>05</i>Clockwork Station', 'Timed gates, switches, moving platforms'),
            ('<i>06</i>Supernova', 'Suns, solar wind, breakable crystals'), ('<i>07</i>Tidewater', 'Tidal planets whose pull rises and falls'), ('<i>08</i>Mirror Maze', 'Glass walls for bank shots'), ('<i>09</i>Repulsor Reef', 'Repulsors that push the ball away'), ('<i>10</i>Grand Tour', 'Long journeys with everything')])}
    </div></section>
{band('../', 'Puttnik brought the share codes, QR codes and Lab pattern that Glidegang’s Course Lab now uses — all of it built with overcli.')}
'''
page('puttnik', 'Puttnik — mini golf across tiny planets', 'Mini golf across tiny planets, for iPhone: 90 holes of gravity, slingshots and black holes. Built with overcli.', 'puttnik', 'puttnik/', puttnik)

# ── Glidegang ───────────────────────────────────────────────────────────
glide = f'''{game_hero('glidegang', '../', 'glider racing', 'Eight gliders. <em>One canyon.</em>', 'Eight pilots launch off a cliff top and dive through canyons, sea stacks, waterfalls and volcano vents — riding updrafts, stealing slipstreams and bumping rivals into rock walls on the way to the landing pad.', ['iPhone · landscape', '8 racers', 'up to 8 on the same Wi-Fi'], 'on an iPhone · Volcano Vents, over a lava river')}
    <section class="sec" style="padding-block: 0 clamp(64px, 8vw, 112px); border: 0"><div class="wrap">{strip([('8', 'racers in every race'), ('6', 'places to race'), ('10', 'items, weighted to the back'), ('60–120 s', 'a race')])}</div></section>
    <section class="sec" style="padding-top: 0; border: 0"><div class="wrap">
      <div class="shots"><figure><img src="../assets/glidegang-canyon.jpg" alt="Red Rock Canyon: diving between canyon walls with an item just picked up" /><figcaption>red rock canyon · 175 km/h, item in hand</figcaption></figure><figure><img src="../assets/glidegang-storm.jpg" alt="Storm Front: racing at night in the rain past wind turbines toward the first gate" /><figcaption>storm front · night, rain and wind turbines</figcaption></figure><figure><img src="../assets/glidegang-thermal.jpg" alt="Red Rock Canyon: a thermal of rising air, +4 metres a second, ahead in the canyon" /><figcaption>red rock canyon · rising air, +4 m/s</figcaption></figure><figure><img src="../assets/glidegang-menu.jpg" alt="The Glidegang menu: Play, Online Rumble, Party, Daily Course and Time Trial" /><figcaption>the menu · online rumble, party, daily course, time trial</figcaption></figure></div>
      <p class="meta" style="margin-top: 18px">Screenshots from an iPhone, from the current build.</p>
    </div></section>
    <section class="sec" id="how"><div class="wrap">
      <div class="head"><div><p class="eyebrow">[ <b>how it flies</b> ]</p><h2>Speed is height.</h2></div><p class="lede">Diving trades altitude for speed, climbing spends it. Updrafts are the only free height — so the race is about reading the air.</p></div>
      {feats([('Always in the pack', 'Slipstreams, short courses and items that favour the back keep all eight racers close.'), ('Rumble', 'Bumps, gusts and shields: contact is part of racing, and funny, never frustrating.'), ('Flow', 'No hard stops. Scrape a wall and bounce off; crash and you’re back in 1.5 seconds.'),
              ('Easy to fly', 'Tilt or one stick. The skill is in racing lines, dive timing and stringing thermals together.'), ('Ten items', 'Bubble Shield, Rocket, Thermal Bomb, a Tether to the racer ahead — and a Storm Cloud for the leader.'), ('Course Lab', 'Lay a route through a map, place gates and thermals, and share it once a bot can finish it.')])}
    </div></section>
    <section class="sec"><div class="wrap row">
      <div><p class="eyebrow">[ <b>six places to race</b> ]</p><h2>Read the air <em>in each.</em></h2><p class="body">Three courses in each, plus a new seeded course every day.</p></div>
      {lst([('Red Rock Canyon', 'Desert arches · strong thermals over sunny rock'), ('Alpine Pass', 'Snowy ridges and cable cars · ridge lift, downdrafts'), ('Tropic Isles', 'Sea stacks and waterfalls · water skimming'), ('Volcano Vents', 'Lava rivers · huge vent thermals, ash clouds'), ('Sky Isles', 'Floating islands · thermal chains, cloud banks'), ('Storm Front', 'Cliffs at night · gusts, rain and lightning')])}
    </div></section>
    <section class="sec"><div class="wrap row">
      <div><p class="eyebrow">[ <b>modes</b> ]</p><h2>Race, Cup, <em>Rumble.</em></h2></div>
      {lst([('Race and Cup', 'A single course, or four with points and a podium'), ('Online Rumble', 'Up to 4 people online, bots fill to 8'), ('Party', 'Up to 8 people on the same Wi-Fi'), ('Time Trial · Daily', 'Race ghosts, and a seeded course every day'), ('Elimination', 'The last racer is out at every section gate'), ('Ring Rush', 'Two minutes of free flight collecting rings')])}
    </div></section>
    <section class="sec"><div class="wrap">
      <div class="head"><div><p class="eyebrow">[ <b>lab notes</b> ] · from the build log</p><h2>Tuned with bots, <em>then with people.</em></h2></div></div>
      <div class="notes"><div class="note"><span class="meta">bots</span><p><b>Bots you can beat.</b> A stand-in new player finishes 2.4th on average on Easy, 5.8th on Normal and 8th on Hard, over eight courses.</p></div>
      <div class="note"><span class="meta">tests</span><p><b>Every course is flyable.</b> 60 tests pass, and a bot finishes every course without crashing more than twice.</p></div>
      <div class="note"><span class="meta">now</span><p><b>On a real iPhone.</b> The screens above are from it. Next: two phones on the same Wi-Fi, then Game Center.</p></div></div>
    </div></section>
{band('../', 'Glidegang is the newest game in the lab: one long overcli session took it through all twelve milestones, with every test passing.')}
'''
page('glidegang', 'Glidegang — eight gliders, one canyon', 'A chaotic glider racing game for iPhone, for 8 racers: canyons, updrafts, slipstreams and gust cannons. Built with overcli.', 'glidegang', 'glidegang/', glide)

# ── How we build ───────────────────────────────────────────────────────
log = [('$', 'Glidegang → Build All', '#8784a6'), ('', 'GLIDEGANG BUILD OK', '#8fe56e'), ('', 'GLIDEGANG TESTS OK (60 passed)', '#8fe56e'), ('', 'bot finish · every course, no more than two crashes', '#8fe56e'),
       ('', 'played in batch mode · menu, hangar, Course Lab, five races, Ring Rush, Time Trial', '#b7b5d1'), ('', 'no game errors logged', '#b7b5d1'), ('!', 'not tried · a real iPhone, two phones on Wi-Fi, Game Center', '#ffd25c')]
logs = ''.join(f'<span style="display: flex; gap: 10px"><i style="font-style: normal; color: #8784a6; width: 10px">{p}</i><span style="color: {c}">{t}</span></span>' for p, t, c in log)

REGISTRY = 'https://github.com/overcodelions/overcli-flow-registry/blob/main/flows/game-from-spec.yaml'
FSTEPS = [('01', 'Plan', 'Architect', 'Claude Fable 5.2', 'Reads CLAUDE.md and the spec, picks the milestones and plans them.', 'plan.md', ''),
          ('02', 'Build', 'Builder', 'Claude Sonnet 5.5', 'Writes the milestones in Unity, compiling in batch mode as it goes.', 'diff', ''),
          ('03', 'Verify', 'Lead', 'Claude Opus 5.5', 'Compiles, runs Build All and every test, lets a bot play, checks the screenshots.', 'verify.md', 'gate'),
          ('04', 'Fix', 'Builder', 'Claude Sonnet 5.5', 'One pass on exactly what verify blocked — or “No changes required.”', 'diff', 'fix'),
          ('05', 'Tests', 'Builder', 'Claude Sonnet 5.5', 'Extends the tests for what was just built, and runs them.', 'tests_report.md', ''),
          ('06', 'Log', 'Lead', 'Claude Opus 5.5', 'Writes spec/BUILD_LOG.md: what passed, and what nobody has tried yet.', 'BUILD_LOG.md', '')]
fsteps = ''.join(f'<li class="fstep {k}"><span class="fn">{n}</span><b>{t}</b><span class="who">{w} · {m}</span><p>{d}</p><code>→ {o}</code>' + ('<span class="fgate">approval gate</span>' if k == 'gate' else '') + '</li>' for n, t, w, m, d, o, k in FSTEPS)
RUNS = [('crater', 'Crater', 'Plan → Build → Review → Tests → Polish', 'One overnight run. Review sent the build back once; then tests, then a polish pass.'),
        ('puttnik', 'Puttnik', 'Plan → Build → Verify', 'One unattended run. Verify sent the build back once, then approved it.'),
        ('glidegang', 'Glidegang', 'One long session', 'All twelve milestones in a single unattended session, before the flow existed.')]
runs = ''.join(f'<li class="{g}"><img src="../assets/{ICON[g]}" alt="" /><span><b>{n}</b><code>{f}</code><span>{t}</span></span></li>' for g, n, f, t in RUNS)
flow_sec = f'''    <section class="sec" id="flow"><div class="wrap">
      <div class="head"><div><p class="eyebrow">[ <b>the flow</b> ] · built with overcli flows</p><h2>Six steps, <em>three models.</em></h2></div><p class="lede">A flow is a recipe overcli runs on its own: each step gets its own model, its own tools and the work of the steps before it. This is the one our games are built with, written down from the runs that built them.</p></div>
      <ol class="flowmap">{fsteps}<li class="fstep you"><span class="fn">→</span><b>We play it</b><span class="who">Lionel &amp; Owen · on an iPhone</span><p>Tilt, touch, two phones on the Wi-Fi, how it feels. Then the next spec change.</p></li></ol>
      <div class="flowfoot"><p class="meta">Runs unattended: every step is local, nothing is committed or pushed, and the verify step goes forward to one fix pass instead of looping back to build.</p><a class="btn btn-line" href="{REGISTRY}" target="_blank" rel="noopener">Get the flow ↗</a></div>
      <ul class="runs">{runs}</ul>
      <p class="meta" style="margin-top: 14px">In overcli: Settings → Flows → the public registry → <b style="color: var(--ink)">Build a game from a spec</b>.</p>
    </div></section>
'''
how = f'''    <section class="hero"><div class="wrap">
      <div class="hero-copy"><p class="eyebrow">[ <b>how we build</b> ]</p><h1>A father, a son, <em>and overcli.</em></h1>
        <p class="lede">We design the games together. overcli — the agent desktop app we also make — builds them with a flow: one model plans, another builds, a third checks the work with Unity’s own tests. <a href="#flow" style="color: var(--ink)">See the flow ↓</a> Then we pick up a phone and play.</p>
        <div class="btns"><a class="btn btn-ink" href="{OVERCLI}" target="_blank" rel="noopener">Meet overcli ↗</a><a class="btn btn-line" href="../">All the games</a></div></div>
      <div class="phone" style="--g: #ffb23d"><span class="scene" style="aspect-ratio: auto; background: #0b0d1c; padding: clamp(18px, 2.4vw, 30px); display: flex; flex-direction: column; gap: 9px; font: 400 clamp(11px, 1vw, 13.5px)/1.5 'Geist Mono', monospace">{logs}</span></div>
    </div></section>
    <section class="sec"><div class="wrap">
      <div class="head"><div><p class="eyebrow">[ <b>the loop</b> ]</p><h2>Spec, build, <em>test, play.</em></h2></div><p class="lede">The agent does the long, careful work. The parts only people can judge — how it feels in your hands — stay ours.</p></div>
      {feats([('The spec', 'Every game starts as one document: its pillars, rules, tuning numbers and milestones. It’s the source of truth for us and for the agent.'),
              ('Built by flows', 'An overcli flow works through the milestones on its own: one model plans, another builds, a third compiles in Unity’s batch mode and runs the tests.'),
              ('Tested before we play', 'A Build All menu runs every test. Bots fly every course and putt every hole; the screenshots are checked.'),
              ('Then we play', 'Tilt, touch, two phones on the Wi-Fi, how it feels — the parts no test can judge. That’s our job.'),
              ('One family', 'Each game copies what it needs from the last one — terrain, share codes, the Lab pattern — and never edits its siblings.'),
              ('Honest notes', 'Every session ends with a build log: what was built, what passed, and what nobody has tried yet.')])}
    </div></section>
{flow_sec}{band('../', 'overcli puts Claude Code, Codex and the other agent CLIs in one window, then lets them work in long sessions, review each other and run in loops. It’s how these games get built — and it’s free and open source.')}
'''
page('how-we-build', 'How we build — Codelions Games Lab', 'How a father and son build iPhone games with a spec, Unity’s tests and overcli.', '', 'how-we-build/', how)
print('pages written')
