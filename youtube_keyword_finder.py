from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
from collections import Counter

def get_video_id(url):
    """Extract video ID from YouTube URL"""
    return url.split("v=")[-1].split("&")[0]

def format_timestamp(seconds):
    """Convert seconds to MM:SS format"""
    mins = int(seconds // 60)
    secs = int(seconds % 60)
    return f"{mins}:{secs:02d}"

def analyze_transcript(video_id):
    """Main analysis function with keyword search"""
    api = YouTubeTranscriptApi()
    
    try:
        # Fetch transcript
        print("\n⏳ Fetching transcript...")
        transcript = api.fetch(video_id, languages=['en'])
        
        # Get full text
        full_text = " ".join([snippet.text for snippet in transcript.snippets])
        
        # Calculate video length
        last_snippet = transcript.snippets[-1]
        video_length = last_snippet.start + last_snippet.duration
        
        # Word frequency analysis
        words = full_text.lower().split()
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'is', 'it', 'that', 'this', 'i', 'you', 'we', 'my', 'your', 'be', 'have', 'with'}
        filtered_words = [w for w in words if w not in stop_words and len(w) > 2]
        common_words = Counter(filtered_words).most_common(10)
        
        # Display basic stats
        print("\n" + "="*60)
        print("📊 YOUTUBE TRANSCRIPT ANALYSIS")
        print("="*60)
        print(f"\n🎥 Video ID: {video_id}")
        print(f"🗣️  Language: {transcript.language}")
        print(f"⏱️  Duration: {int(video_length // 60)}m {int(video_length % 60)}s")
        print(f"💬 Total Snippets: {len(transcript.snippets)}")
        print(f"📝 Total Words: {len(words)}")
        
        print("\n🔥 TOP 10 MOST COMMON WORDS:")
        for word, count in common_words:
            bar = "█" * (count // 2)  # Visual bar
            print(f"   {word:15} → {count:3} times {bar}")
        
        # Keyword search feature
        print("\n" + "="*60)
        print("🔍 KEYWORD SEARCH")
        print("="*60)
        keyword = input("\nEnter keyword to search (or press Enter to skip): ").strip()
        
        if keyword:
            matches = []
            for snippet in transcript.snippets:
                if keyword.lower() in snippet.text.lower():
                    matches.append(snippet)
            
            if matches:
                print(f"\n✅ Found '{keyword}' {len(matches)} times:\n")
                for snippet in matches:
                    timestamp = format_timestamp(snippet.start)
                    youtube_link = f"https://youtube.com/watch?v={video_id}&t={int(snippet.start)}s"
                    print(f"⏱️  [{timestamp}] {snippet.text}")
                    print(f"   🔗 {youtube_link}\n")
            else:
                print(f"\n❌ Keyword '{keyword}' not found in transcript.")
        
        # Save option
        print("\n" + "="*60)
        save = input("💾 Save full transcript to file? (y/n): ").strip().lower()
        if save == 'y':
            filename = f"{video_id}_transcript.txt"
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"YouTube Video: https://youtube.com/watch?v={video_id}\n")
                f.write(f"Language: {transcript.language}\n")
                f.write(f"Duration: {int(video_length // 60)}m {int(video_length % 60)}s\n")
                f.write("="*60 + "\n\n")
                f.write(full_text)
            print(f"✅ Saved to {filename}")
        
    except TranscriptsDisabled:
        print("❌ Error: Transcripts are disabled for this video.")
    except NoTranscriptFound:
        print("❌ Error: No transcript found.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

def main():
    """Main program loop"""
    print("╔" + "="*58 + "╗")
    print("║" + " "*15 + "🎬 YOUTUBE KEYWORD FINDER" + " "*18 + "║")
    print("╚" + "="*58 + "╝")
    
    while True:
        print("\n" + "-"*60)
        url = input("Enter YouTube URL (or 'quit' to exit): ").strip()
        
        if url.lower() == 'quit':
            print("\n👋 Thanks for using YouTube Keyword Finder!")
            break
        
        if 'youtube.com' not in url and 'youtu.be' not in url:
            print("❌ Invalid YouTube URL. Try again.")
            continue
        
        video_id = get_video_id(url)
        analyze_transcript(video_id)
        
        # Ask if they want to analyze another video
        another = input("\n🔄 Analyze another video? (y/n): ").strip().lower()
        if another != 'y':
            print("\n👋 Thanks for using YouTube Keyword Finder!")
            break

if __name__ == "__main__":
    main()
