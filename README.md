# Claude Code - Advent of Code 2025

![Python](https://img.shields.io/badge/python-3.x-blue)
![Claude](https://img.shields.io/badge/claude-sonnet--4.5-purple)
![Autonomous](https://img.shields.io/badge/autonomous-91%25-green)
![Advent of Code](https://img.shields.io/badge/advent--of--code-2025-red)

https://github.com/user-attachments/assets/bbb2d8fa-72dc-4224-acbf-43486058dc24

> **TL;DR**: I gave Claude Code a single instruction file and it autonomously solved 11 days of Advent of Code 2025. It browsed the web, read puzzles, wrote code, tested solutions, and submitted answers - all without human intervention. **Zero lines of code written by hand. 20/22 challenges solved (91%).**

## By The Numbers

- 🤖 **0** lines of code written by hand
- ✅ **20/22** challenges solved (91% success rate)
- 🧠 **Model**: Claude Sonnet 4.5
- ⚡ **Autonomous**: Web browsing → Code writing → Answer submission
- 📁 **~42** Python files generated
- 🔄 **Self-correcting**: Automatically retried when answers were wrong

## What if AI could solve coding challenges completely autonomously?

I gave [Claude Code](https://claude.com/claude-code) powered by **Claude Sonnet 4.5** a single instruction file and watched it autonomously solve [Advent of Code 2025](https://adventofcode.com/2025) - browsing the web, reading puzzles, writing code, and submitting answers without human intervention.

## About This Year's Advent of Code

2025 marks a significant shift for Advent of Code. For the first time ever, there are only 12 questions instead of the traditional 25, and the global leaderboard has been removed (though private leaderboards still exist).

Let's be honest - the rise of LLMs has kind of killed the manual solving fun for many people. But here's the thing: if you can't beat them, let them join you!

## What Makes This Different?

This isn't just about using AI to help code - that's common now. This is about **full autonomy**:

1. **Zero Human Code**: Not a single line of code was written by hand - only `INSTRUCTIONS.md` was human-written
2. **Complete Workflow Automation**: Claude handled browsing, reading, understanding, coding, testing, and submitting
3. **Web Interaction**: Navigated websites, read content, submitted forms autonomously
4. **Self-Correction**: Analyzed failures and adjusted approach when answers were wrong
5. **Full Transparency**: Conversation exports in `claude_export.txt` show Claude's entire reasoning process

## The Experiment: Fully Autonomous AI Development

**This entire repository was created autonomously by [Claude Code](https://claude.com/claude-code)** powered by **Claude Sonnet 4.5**, using only the `INSTRUCTIONS.md` file as guidance. No code was written by hand. Zero. Nada.

Here's what Claude Code did all by itself:

- Browsed the Advent of Code website using the Claude Chrome plugin
- Read and understood each day's puzzle (including all that quirky flavor text)
- Developed solution strategies
- Wrote and tested Python code
- Submitted answers automatically
- Self-corrected when answers were wrong by rethinking the approach and iterating

Day 1 was solved manually (hence not included in this repo), but Days 2-12 were 100% Claude Code's work.

### How It Worked

Each day was manually triggered to avoid burning through tokens unnecessarily. But here's the cool part: this entire process could be fully automated using Claude Code's parallel agents feature. Imagine launching 12 agents simultaneously, each tackling a different day concurrently. That's the future we're living in.

### Command Used (And Why You Shouldn't Use It)

The command used was:

```bash
claude --chrome --dangerously-skip-permissions
```

**This is a terrible way to run Claude Code.** The `--dangerously-skip-permissions` flag bypasses all safety checks, and the Claude Chrome extension has critical vulnerabilities. This was done purely for experimentation purposes in a controlled environment.

**Do not run this command unless you fully understand the security implications.** For production use, always use proper permission controls and consider the security risks of browser automation.

## Repository Structure

```
advent-2025/
├── day_02/          # Day 2 solutions
├── day_03/          # Day 3 solutions
├── day_04/          # Day 4 solutions
├── day_05/          # Day 5 solutions
├── day_06/          # Day 6 solutions
├── day_07/          # Day 7 solutions
├── day_08/          # Day 8 solutions
├── day_09/          # Day 9 solutions
├── day_10/          # Day 10 solutions
├── day_11/          # Day 11 solutions
├── day_12/          # Day 12 solutions
└── INSTRUCTIONS.md  # The only human-written file
```

## What's Inside Each Day

- `claude_export.txt` - Exported conversation showing Claude's thought process
- `part1.py` - Solution for part 1
- `part2.py` - Solution for part 2
- `input.txt` - Puzzle input
- `example.txt` - Example test cases (when applicable)
- Various test and debug files as needed

## Running the Solutions

```bash
python day_XX/part1.py
python day_XX/part2.py
```

## Requirements

- Python 3.x
- A sense of wonder about what AI can do

## Try It Yourself

Want to replicate this experiment?

1. Install [Claude Code](https://claude.com/claude-code)
2. Check out `INSTRUCTIONS.md` in this repo to see the instructions used
3. Set up your own Advent of Code puzzles
4. Run your experiment (with proper security precautions!)

**Important**: See the security warning section above before attempting this yourself.

## Progress & Limitations

- **Day 1**: Solved manually (not included)
- **Days 2-8**: Fully completed by Claude Code ✓
- **Day 9 Part 1**: Completed ✓
- **Day 9 Part 2**: Not completed (Claude hit a wall here)
- **Days 10-11**: Fully completed by Claude Code ✓
- **Day 12 Part 1**: Completed ✓
- **Day 12 Part 2**: Not available (requires Day 9 Part 2 completion)

**Success Rate**: 20 out of 22 challenges (91%)

Even AI has its limits. For now.

## Demo

**[TODO: Add screenshots of Claude Code in action]**

**[TODO: Add video walkthrough showing the autonomous process]**

Want to see how Claude approached each problem? Check out the `claude_export.txt` files in each day's folder - they contain the complete conversation transcripts showing Claude's reasoning, debugging, and problem-solving process.

## Why This Matters

We're witnessing the emergence of truly autonomous coding agents. This isn't about replacing developers - it's about amplifying what's possible.

This experiment demonstrates that with the right instructions, AI can now:

- Navigate complex websites autonomously
- Understand nuanced programming requirements
- Write, test, and debug code independently
- Learn from failures and self-correct
- Complete end-to-end workflows without human intervention

The age of autonomous coding agents isn't coming - it's already here. The future of software development isn't human OR AI - it's human AND AI working together, with AI handling increasingly complex autonomous tasks while humans provide direction and oversight.

---

**Keywords**: AI automation, autonomous coding, Claude AI, Advent of Code, AI agents, code generation, LLM programming, autonomous development, Claude Code, Sonnet 4.5, zero human code, fully autonomous AI

**Topics**: `artificial-intelligence` `automation` `advent-of-code` `claude-ai` `autonomous-agents` `code-generation` `python` `llm` `ai-coding`

