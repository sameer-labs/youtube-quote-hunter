# 🎬 YouTube Keyword Finder

*Because sometimes you just need to know how many times someone said "bro" in a 45-minute video.*

## What's This?

Honestly? I got tired of rewatching entire videos just to find that one quote that hit different. You know the feeling—you're watching a podcast, someone drops an absolute banger of a line, and two weeks later you're like "wait, what video was that in?" 

So I built this little tool. It grabs YouTube transcripts, lets you search for keywords, and gives you clickable timestamps. No more scrubbing through progress bars like a caveman.

Also, yes, I did use this to count how many times Flamefrags says "bro" in his videos. The answer? Too many. Way too many. 😭

## Why You Might Want This

**If you're a student:**
- Find that one concept your prof mentioned in a 3-hour lecture
- Actually study efficiently for once
- Pretend you watched the whole thing (I won't tell)

**If you're a dev:**
- Jump to specific parts of tutorials without guessing
- Build a knowledge base from tech talks
- Track how often people say "it depends" in programming videos (spoiler: a lot)

**If you're just bored:**
- Count catchphrases
- Find embarrassing moments in old videos
- Discover your favourite creator's most-used words

Or you know, just mess around with it. That's cool too.

## Getting Started

### You'll Need
```bash
pip install youtube-transcript-api
```

That's it. One dependency. I'm not trying to install half of npm here.

### Running It
```bash
python youtube_keyword_finder.py
```

Paste a YouTube URL when it asks. Search for whatever. It's pretty straightforward.

## What It Actually Does
```
🎬 YOUTUBE KEYWORD FINDER
────────────────────────────────────────────────────────────

Enter YouTube URL: [paste literally any YouTube video]

⏳ Fetching transcript...

📊 YOUTUBE TRANSCRIPT ANALYSIS
════════════════════════════════════════════════════════════

🎥 Video ID: dQw4w9WgXcQ
🗣️  Language: English
⏱️  Duration: 3m 33s
💬 Total Snippets: 47
📝 Total Words: 312

🔥 TOP 10 MOST COMMON WORDS:
   never          →  12 times ██████
   gonna          →  12 times ██████
   you            →  10 times █████

🔍 KEYWORD SEARCH
════════════════════════════════════════════════════════════

Enter keyword to search: never

✅ Found 'never' 12 times:

⏱️  [0:01] Never gonna give you up
   🔗 https://youtube.com/watch?v=dQw4w9WgXcQ&t=1s

[you get the idea]
```

## Features (The Actual Useful Stuff)

- **Search with Timestamps** - Type a word, get every moment it's mentioned with clickable links
- **Word Frequency** - See what words show up most (filters out boring ones like "the" and "um")
- **Save Transcripts** - Export everything to a text file because why not
- **Multi-language** - Works with whatever language YouTube supports
- **Multiple Videos** - Analyse a bunch in one go without restarting

## Real Talk: What I Use This For

1. **Finding quotes** - I watch a lot of motivational/productivity content, and this helps me bookmark the good stuff
2. **Learning faster** - Jump straight to the parts of tutorials I actually need
3. **Memes** - Counting how many times people say things is genuinely hilarious
4. **Future projects** - This is lowkey practice for building a personal AI agent that can learn from everything I watch

Number 4 is the real reason. I want an AI that remembers every video I've watched and can pull insights when I ask. This is step one. Baby steps.

## Known Issues (aka Things I Haven't Fixed Yet)

- Videos without captions won't work (duh)
- Sometimes YouTube auto-captions are hilariously wrong
- No fancy GUI because I'm lazy and terminal apps are cool
- The word frequency filter isn't perfect—you might see some weird stuff

## Contributing

If you want to add features or fix bugs, go for it! I'm still learning, so I'd honestly love to see what you come up with. Just open an issue or PR, and we can figure it out.

Some ideas if you're bored:
- Add support for playlist processing
- Make a GUI version (I believe in you)
- Better word filtering
- Export to markdown with timestamps
- Literally anything else you think would be cool

## The Boring Legal Stuff

MIT License. Use it however you want. Sell it. Turn it into an NFT. I don't care. Just don't sue me if YouTube changes its API and this breaks.

## Shoutouts

- The `youtube-transcript-api` library for doing all the hard work
- Flamefrags for saying "bro" enough times to inspire this entire project
- You, for actually reading this README instead of just cloning and running
- Coffee, my one true love

---

Made by a CS student who got tired of rewatching videos.

If this saved you 10 minutes of your life, consider it a win. ⭐ It if you want, or don't—I'm not your dad.

**Current "bro" count in Flamefrags videos: classified** 😂
