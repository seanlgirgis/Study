**Project: Capital-One-CodeSignal-Prep-2026**  
**Sprint: 150.Lead-Data-Engineer-CodeSignal-Sprint**  
**Date: February 13, 2026**  
**Session: Day 1 – Logistics & Rules Clarification**

### What kind of help is allowed during the Capital One CodeSignal proctored assessment?

**Short answer (based on 2024–2026 candidate reports + official CodeSignal / Capital One rules):**

**Almost nothing.**  
This is a **closed-book, no-external-resources, heavily proctored coding test**.

### What is typically **allowed** during the test
- The built-in CodeSignal code editor (Python 3.x environment)
- Standard Python built-in functions & modules that come with a clean Python install (list, dict, set, str methods, range, enumerate, sorted, max/min, sum, etc.)
- `collections` module → `Counter`, `deque`, `defaultdict`
- `heapq`, `bisect`, `math`, `itertools`, `functools` (including `@cache` / `@lru_cache`)
- Basic typing (`from typing import List, Dict, Optional, etc.`)
- Copy-paste **within your own code** (you can copy your own previous solutions if you typed them during the test)
- **No external documentation**, **no Google**, **no LeetCode**, **no personal notes**, **no phone**, **no second monitor**, **no chat**, **no AI**

### What is **explicitly prohibited** (and monitored)
- Looking up anything on the internet (Google, Stack Overflow, GeeksforGeeks, etc.)
- Opening any other browser tab or application
- Using AI tools (ChatGPT, Grok, Claude, Copilot, etc.) — Capital One explicitly forbids generative AI in the email you received
- Referring to physical notes, textbooks, cheat sheets
- Having someone else in the room or communicating with anyone
- Using a second computer / phone / tablet
- Screen sharing, remote desktop, virtual machines (most are detected anyway)

### What the proctoring system actually watches (CodeSignal GCA proctoring — 2025/2026 version)
- Webcam (full face must stay in frame, good lighting, no one else enters)
- Screen recording (they see everything you open / switch to)
- Tab switching / application switching detection
- Keystroke + mouse movement patterns (very unnatural patterns can trigger flags)
- Audio (mic on — detects talking / unusual background noise)
- ID verification at start (government ID + room scan in some cases)

### Real candidate experiences (aggregated from Glassdoor, Blind, Reddit 2024–2026)
- “You get syntax highlighting and that’s it. No autocomplete beyond basic Python, no documentation lookup.”
- “I tried to alt-tab to notes — got warning popup within seconds.”
- “They really don’t let you search anything. People who tried got flagged / failed to advance.”
- “Know your templates cold: BFS, DFS, sliding window, two pointers, monotonic stack. No time to derive from scratch if you don’t remember.”

### Practical advice for Feb 23 attempt
You **cannot** rely on looking things up mid-test.  
That means:

- You need to be able to write common patterns **from muscle memory**:
  - BFS/DFS grid templates
  - Sliding window variable-size
  - Two-pointer sorted / same-direction
  - Prefix sum / cumulative
  - Counter + most_common
  - Heapq min/max heap
  - Basic class design (e.g. bank account sim)

- If you forget exact syntax (e.g. `heapq.heappush`, `bisect.bisect_left`), you’re expected to either:
  - Recall it
  - Write a correct but slightly slower alternative
  - Get partial credit with brute force / suboptimal solution

### Updated Day 1 focus (given this constraint)
Since lookup is **not** an option during the test, we shift priority to **memorization + fast recall** of high-frequency patterns.

**Today’s drills (Phase A – Foundation Tier)**  
Target: Solve these **without looking anything up** (simulate test conditions):

1. LeetCode 1 – Two Sum (hash map complement)
2. LeetCode 217 – Contains Duplicate (set or Counter)
3. LeetCode 560 – Subarray Sum Equals K (prefix sum + hash map)
4. LeetCode 974 – Subarray Sums Divisible by K (prefix sum modulo)

**Action for you:**
- Time yourself: aim < 10–12 min per easy problem
- Write clean, typed code **without searching**
- Then paste here → I’ll run it through code_execution, check correctness + style

Want me to give you clean problem statements (without solutions) so you can attempt blind first?

Or do you want to adjust Day 1 plan now that we confirmed no lookup is possible?

Let me know how you want to proceed.