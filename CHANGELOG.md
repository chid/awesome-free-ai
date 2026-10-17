# Changelog

Every edition of this list is a dated snapshot. Free tiers move fast, so what
changed matters as much as what's on the list.

The machine-readable record lives in [`history.csv`](history.csv),
[`paid_history.csv`](paid_history.csv) and [`local_history.csv`](local_history.csv) — those
files are append-only and are the source of truth. This file is the human-readable summary.

Format loosely follows [Keep a Changelog](https://keepachangelog.com).

## [2026-10-17] — Weekly local refresh: a 34.6k-star roleplay frontend, a model-swapping proxy, Weaviate, and OpenAI's open weights

This refresh added 5 tools. It builds on the still-open, unmerged
[#9](https://github.com/chid/awesome-free-ai/pull/9) refresh below (96 local
tools) on the same `refresh/2026-10` branch, taking the running total from
96 to **101 local tools**. Corrected the README's Local Tools badge to match
(96 → 101); the Paid Tools badge was already accurate at 28.

### Added
- **SillyTavern** — Web UI. Locally installed LLM frontend for power users
  with character cards, World Info lorebooks, group chats, and vector-store
  long-term memory; pairs with local backends (KoboldCpp, TextGen/oobabooga,
  Ollama, LM Studio) or cloud APIs. AGPL-3.0, 34.6k stars, commits through
  Oct 14 2026.
- **llama-swap** — Local Runner. Single-binary Go proxy that inspects the
  `model` field of incoming OpenAI/Anthropic-compatible requests and starts
  or swaps the matching local backend (llama.cpp, vLLM, etc.) on demand, so
  one stable endpoint can serve many models. MIT, 6k stars, commits through
  Oct 14 2026.
- **Weaviate** — Embeddings / RAG. Self-hostable hybrid (vector + keyword)
  search database with multi-tenancy and native local embedding/reranking
  modules; Community Edition runs free via Docker. BSD-3-Clause core
  (Enterprise-only `wl/` folder is separately commercially licensed), 16.9k
  stars, commits through Oct 16 2026.
- **gpt-oss** — Open Weights (LLM). OpenAI's first open-weight model family
  since GPT-2 (gpt-oss-120b, gpt-oss-20b) for reasoning and agentic tool use,
  with reference PyTorch/Triton/Metal implementations and day-one Ollama/LM
  Studio support. Apache-2.0, 20.5k stars, commits through Oct 12 2026.
- **VibeVoice** — Audio & Speech. Microsoft's open speech family spanning
  long-form multi-speaker TTS (up to 90 min), real-time streaming TTS, and
  long-audio ASR (up to 60 min), including a CPU-only BitNet ASR variant;
  fills a distinct long-form/multi-speaker niche alongside this list's
  existing voice-cloning TTS tools. MIT, 54.9k stars, commits through Oct 8
  2026.

No cross-pathway duplicates found in `resources.csv` or `paid_resources.csv`,
and no drift (archival, relicensing, renaming) turned up in the existing
rows this week.

## [2026-10-10] — Weekly local refresh: 14 additions across code agents, serving, fine-tuning, and open weights; retired a dormant desktop client

This refresh added 14 tools and removed 1 dormant entry, taking the total
from 83 to 96 local tools. Verified the README's local/paid/free counts
against the actual CSV row counts via `python3 update.py`'s audit (72 free,
28 paid, 96 local).

### Added
- **Crush** (Charmbracelet) — Code Assistant. Terminal agentic coding
  assistant with MCP server support and auto-discovery of local model
  providers (Ollama, llama.cpp, LM Studio, MLX). FSL-1.1-MIT (fair-source,
  converts to MIT after 2 years), v0.98.1 released Oct 9 2026.
- **fast-agent** — Agent Framework. MCP-native Python framework for
  building, running, and evaluating agents with first-class local-model
  support via Ollama/llama.cpp. Apache-2.0.
- **Letta** — Agent Framework. Self-hostable stateful-agents platform with
  long-term memory, runs fully local against Ollama/LM Studio. Apache-2.0.
- **Agno** — Agent Framework. Python multi-agent framework with native
  Ollama model classes and an MCP tools layer. Apache-2.0.
- **KTransformers** — Serving Engine. Heterogeneous CPU+GPU inference
  framework that offloads large MoE models (DeepSeek-V3/R1) onto
  consumer-grade hardware via kernels injected into Hugging Face
  Transformers. Apache-2.0, v0.7.1 released Sep 15 2026.
- **Harbor** — Local Runner. Docker Compose launcher that wires up a
  complete local LLM stack (backends + frontends) in one command — same
  spirit as the already-listed RamaLama. Apache-2.0.
- **Gemma 4** (Google DeepMind) — Vision & Multimodal. First Apache-2.0
  Gemma generation, with native multimodal (image/video, audio on smaller
  sizes) across all sizes. Family launched Apr 2 2026.
- **LTX-2.5** (Lightricks) — Image & Video Gen. 22B open-weight video+audio
  diffusion model with ComfyUI support and GGUF quants. LTX-2.x Community
  License (free under $10M revenue, same shape as the already-listed
  HunyuanVideo-1.5/FLUX 3).
- **HiDream-O1-Image** — Image & Video Gen. 8B unified transformer for
  text-to-image, instruction editing, and personalization on a single
  consumer GPU. MIT.
- **LongCat-2.0** (Meituan) — Open Weights (LLM). 1.6T/~48B-active MoE with
  claimed 1M-token context, datacenter-only like the already-listed Kimi K3
  / MiniMax-M3; community GGUF/Ollama quants available. MIT.
- **PMetal** — Fine-tuning / Quant. Rust Apple Silicon fine-tuning framework
  (LoRA/QLoRA/full/DPO/KTO/GRPO) filling the CUDA-centric gap next to
  Unsloth/Axolotl/LLaMA-Factory. Dual MIT/Apache-2.0.
- **LLM Compressor** (vLLM project) — Fine-tuning / Quant. Quantization
  library (GPTQ/AWQ/SmoothQuant/FP8/NVFP4) producing compressed-tensors
  checkpoints for local serving. Apache-2.0.
- **AIPerf** — Hardware / Benchmarking. NVIDIA's actively-developed
  successor to genai-perf/perf_analyzer for benchmarking self-hosted
  inference servers; fills a second slot alongside LocalScore with a
  server-throughput focus. Apache-2.0.
- **EvalScope** (ModelScope) — Evaluation & Harnesses. Evaluation framework
  covering capability/RAG/agent/perf benchmarks against local
  OpenAI-compatible endpoints. Apache-2.0.

### Removed
- **GPT4All** (Desktop Client) — dormant: last commit on the `main` branch
  is 2025-05-27, last tagged release (v3.10.0) is from 2025-02-25, well
  outside the 6-month maintenance bar applied to this list. Repo isn't
  archived, just inactive; worth re-adding if development resumes.

### Considered but not added (this week)
- **NVIDIA Dynamo** / **llm-d** / **GPUStack** — datacenter-cluster
  serving-orchestration layers over vLLM/SGLang/TensorRT-LLM; excluded per
  the stricter bar set in the 2026-10-03 refresh (not a tool a reader runs
  on their own machine).
- **Sonar** (formerly Aphrodite Engine, now under `dphnAI`) — vLLM-based
  quantized serving engine; technically qualifies, but passed over as
  redundant with the already-listed vLLM/SGLang/ExLlamaV3/mistral.rs for
  this week's batch.
- **Cline**, **Aider**, **OpenCode**, **Kilo Code** — all genuinely capable
  of running fully offline against Ollama/LM Studio, but already correctly
  placed in `resources.csv` as general BYOK coding agents (not local-only
  tools); not duplicated here. See PR body for the one-tool-one-pathway note.

## [2026-10-09] — Renamed the repository and added upstream review checks

Renamed the repository to `chid/awesome-free-ai` and updated the published-site
and repository links. Added a weekly GitHub Actions check for missing providers
from `awesome-free-llm-apis` and newly listed model pages on models.fyi; both
sources create review issues rather than adding entries automatically.

## [2026-10-07] — Added a guide to following AI developments

Added [`STAY_CURRENT.md`](STAY_CURRENT.md), a curated set of newsletters, blogs,
podcasts, YouTube channels, research feeds, and communities, plus a low-noise
routine for keeping up. Linked it from the live directory and README without
changing the tool catalog or its counts.

## [2026-10-03] — Weekly local refresh: a 48.7k-star agent framework, an embeddable Rust runner, and a quantization toolkit

This refresh added 4 tools (76 → 80); merging with the separately-landed
FLUX 3 / Qwen Omni additions below brings the total to 83 local tools.
Verified the README's local/paid/free counts against the actual CSV row
counts via `python3 update.py`'s audit (72 free, 28 paid, 83 local) — no
drift found in existing rows this week.

### Added
- **nanobot** (HKUDS) — Agent Framework. Ultra-lightweight, self-hosted
  personal AI agent framework in Python with a WebUI, terminal UI, long-term
  memory, MCP tools, multi-agent delegation, and an OpenAI-compatible API;
  connects to Ollama or any local OpenAI-compatible server. MIT, 48.7k stars,
  v0.3.5 released Sep 15 2026.
- **NobodyWho** — Local Runner. Embeddable Rust inference engine built on
  llama.cpp for running GGUF models fully offline inside games and apps, with
  bindings for Godot, Flutter, React Native, Swift, Kotlin, and Python;
  EUPL-1.2.
- **GPTQModel** (ModelCloud) — Fine-tuning / Quant. Extensible quantization
  toolkit covering GPTQ, AWQ, GGUF, EXL3, FP8, and QQQ across NVIDIA, AMD,
  Intel, and Apple Silicon — fills a general-purpose quantization gap next to
  the already-listed finetuning-focused Unsloth/Axolotl/LLaMA-Factory.
  Apache-2.0 core.
- **HunyuanVideo-1.5** (Tencent) — Image & Video Gen. Lightweight open-weight
  text-to-video / image-to-video diffusion model (8.3B params) running on
  ~14GB consumer VRAM; custom Tencent Hunyuan Community License (commercial
  use allowed outside EU/UK/South Korea, >100M MAU needs separate
  permission) — same license-restriction pattern as the already-listed Kimi
  K3 and MiniMax-M3 rows.

### Considered but not added
- **NVIDIA Dynamo** / **llm-d** — open-source disaggregated-serving
  orchestration layers over vLLM/SGLang/TensorRT-LLM; excluded as
  datacenter-cluster orchestration tooling rather than a tool a reader runs
  on their own machine, which is a stricter bar than this list's existing
  datacenter-class **TokenSpeed** entry.
- Assorted single-file VRAM calculators (e.g. `llm-vram-calculator` forks) —
  numerous small, thinly-differentiated hobby scripts; none stood out as the
  clear best-in-class complement to the already-listed **LocalScore**.
- **Breeze TTS 2** — strong open-weight TTS leaderboard result, but weights
  are research/non-commercial only under the BreezeBlue license with no
  self-hosted commercial path; code wrapper (Apache-2.0) alone isn't useful
  without the weights, so left out pending a clearer license.

### Verified, no drift
- Spot-checked **Goose** (`aaif-goose/goose`) and **TokenSpeed**
  (`lightseekorg/tokenspeed`) for archival/rename risk — both active;
  `block/goose` redirects to the already-listed `aaif-goose/goose` URL, so no
  edit needed.

## [2026-10] — Local additions: FLUX 3 and the Qwen Omni family + model timeline prompt

Three open-weight additions to `local_resources.csv`, researched 2026-10-03:

- **FLUX 3 (Black Forest Labs)** (Image & Video Gen) — multimodal video+audio/
  image/action foundation model on the Self-Flow backbone; FLUX 3 Action 7B open
  weights shipped 2026-09-22, FLUX 3 Dev open-weight backbone announced for
  later 2026 (Early Access 2026-07-23)
- **Qwen3-Omni** (Vision & Multimodal) — open-weight 30B-A3B omni-modal MoE
  (Apache-2.0, Sep 2025): text/image/audio/video in, text or real-time speech out
- **Qwen3.5-Omni** (Vision & Multimodal) — next-generation omni-modal LLM
  (Mar 2026); the Light variant ships open weights for local GPUs while the
  Plus tier and Qwen3.8-Omni-Flash (Sep 2026) are API-only

Also added [`models_viz_prompt.md`](models_viz_prompt.md) — a one-time setup
prompt to build an open-weights model release timeline (`models.html` +
`model_releases.csv`), seeded from models.fyi and applying a rolling two-year
window with a `notable` escape hatch for classics.

The timeline itself is now built: [`models.html`](models.html) ships seeded
with 75 releases — 15 notable classics plus 60 in the window, 41 with open
weights shipped and FLUX 3 Dev announced — backed by `model_releases.csv` and
its append-only `model_releases_history.csv`.

## [2026-09-26] — Weekly local refresh: Rust serving, AMD's Lemonade, and two new frontier open-weight MoEs

76 local tools (was 65). Verified the README's local/paid/free counts against
the actual CSV row counts via `python3 update.py`'s audit (72 free, 28 paid,
76 local) and corrected the stale "65 tools" figure for `local_resources.csv`.

### Added
- **Lemonade SDK** (AMD) — Local Runner. Local AI server that auto-detects
  GPU/NPU and serves optimized LLM/image/speech models via an
  OpenAI/Anthropic/Ollama-compatible API; Apache-2.0.
- **mistral.rs** — Serving Engine. Rust-based inference/serving engine across
  45+ architectures (text/vision/video/audio) with OpenAI/Anthropic-compatible
  APIs; MIT.
- **Cherry Studio** — Desktop Client. Electron desktop AI client unifying
  chat, agents, and MCP tool calling across cloud and local (Ollama/LM Studio)
  backends; AGPL-3.0.
- **LibreChat** — Web UI. Self-hosted multi-provider chat platform with
  agents, MCP, and code interpreter, runnable entirely against local/self-hosted
  inference; MIT.
- **smolagents** (Hugging Face) — Agent Framework. Barebones code-writing
  agent library with first-class local execution via transformers/Ollama;
  Apache-2.0.
- **LLaMA-Factory** — Fine-tuning / Quant. Zero-code CLI + web UI (LLaMA
  Board) for LoRA/QLoRA/full fine-tuning across 100+ model families;
  complements the already-listed Unsloth/Axolotl with the widest single-tool
  model coverage. Apache-2.0.
- **LanceDB** — Embeddings / RAG. Embedded (in-process), serverless vector
  database for local multimodal RAG — a lighter-weight complement to the
  already-listed Qdrant server; Apache-2.0.
- **Kimi K3** (Moonshot AI) — Open Weights (LLM). Frontier open-weight MoE
  (2.8T total, 16-of-896 experts active) with native multimodal input and 1M
  context; ships under a custom Kimi K3 License (free for most uses).
- **MiniMax-M3** — Open Weights (LLM). Open-weight mixed-modality MoE (~428B
  total, ~23B active) with 1M context and MiniMax Sparse Attention; custom
  Community License.
- **TADA** (Hume AI) — Audio & Speech. Open speech-language model using
  synchronized token alignment for low-hallucination long-form TTS in 1B/3B
  sizes; MIT code, Llama 3.2 Community License weights.
- **lmms-eval** — Evaluation & Harnesses. Multimodal (text/image/video/audio)
  evaluation toolkit across 30+ model families — fills a gap next to this
  list's existing text-only evaluation harnesses; Apache-2.0.

### Considered but not added
- **opencode** (sst/opencode) — already correctly listed in `resources.csv`
  as **OpenCode** (free pathway, local models via Ollama also supported)
  alongside the separate **OpenCode Go** paid plan; not local-only, so it
  stays a freemium pair rather than duplicating into this list.
- **LTX-2** (Lightricks) — open-weight audio+video diffusion model; still
  excluded for the same reason as last week's "LTX-2.5" rejection — it ships
  under a custom Community License with a revenue-based commercial threshold
  rather than a standard OSI license, and unlike this week's Open Weights
  (LLM) additions there's no established precedent for that in the Image &
  Video Gen category (its existing rows are all GPL/AGPL/Apache).
- **GPUStack** — reconsidered, still excluded: a GPU-cluster orchestrator
  layered on vLLM/SGLang rather than a serving engine in its own right.

## [2026-09-25] — Weekly local refresh: containers, red-teaming, and a DeepSeek V4 update

65 local tools (was 60). Verified the README's local/paid counts against the
actual CSV row counts (65 local, 28 paid — the paid count was already correct;
the earlier `paid_resources.csv` count checked out via `python3 update.py`'s
audit, which skips a stray blank trailing line that a naive line count does
not).

### Added
- **RamaLama** (Red Hat / containers.io) — Container-native CLI that
  auto-detects your GPU and pulls a hardened OCI image bundling llama.cpp,
  vLLM, or MLX, run via Podman/Docker; MIT.
- **VoxCPM2** (OpenBMB) — Tokenizer-free, diffusion-autoregressive TTS model
  with natural-language voice design and zero-shot voice cloning across 30
  languages.
- **garak** (NVIDIA AI Red Team) — Open-source LLM vulnerability scanner
  (50+ probes for prompt injection, jailbreaks, data leakage); a distinct
  adversarial-security focus versus the capability-eval harnesses already
  listed.
- **Axolotl** — Config-driven (YAML) multi-GPU fine-tuning framework
  (LoRA/QLoRA/full/DPO/GRPO via FSDP/DeepSpeed); complements the already-listed
  Unsloth, which is tuned for single-GPU speed rather than multi-GPU scale.
- **Apertus 1.5** (EPFL/ETH Zurich/CSCS) — Fully open multilingual LLM family
  notable for publishing complete training data recipes alongside weights, not
  just the weights themselves.

### Edited (version bump)
- **DeepSeek-R1 / V3 → DeepSeek-R1 / V4** — DeepSeek-V4-Pro/V4-Flash (MIT,
  1M-token context) supersede the V3 line as the flagship open-weight MoE
  models; R1 remains current for reasoning. URL updated to the V4-Pro model
  card.

### Considered but not added
- **OpenCode** — already correctly listed in `resources.csv` (free pathway;
  bring-your-own-key or free providers, with local models via Ollama also
  supported) alongside a separate **OpenCode Go** paid plan in
  `paid_resources.csv`. Not local-only, so it stays a freemium pair in the
  free/paid pathways rather than duplicating into this list.
- **OpenClaw** (Agent Framework) — self-hosted personal agent runtime; skipped
  after research found wildly inconsistent star counts (68k–390k depending on
  source) and numerous near-identical mirror repos, which reads as
  manipulated/SEO-farmed metrics rather than a reliably verifiable project.
- **LTX-2.5** (Image & Video Gen) — open-weight video model, but ships under a
  custom "Community License" with a revenue-based commercial threshold rather
  than a standard OSI license like the rest of this category (GPL/AGPL/Apache).
- **GPUStack** (Serving Engine) — legitimate and active, but it's a cluster
  orchestrator layered on top of vLLM/SGLang/TensorRT-LLM rather than a serving
  engine in its own right; didn't fit the category cleanly.
- **DeepSeek Harness (dsh)**, **Juggler**, **GPTQModel**, **IBM Granite 4.2** —
  active and plausible, but either explicitly labeled an early/unstable
  developer preview, too new to judge maturity, or redundant with an
  already-listed tool covering the same niche.

### Cross-pathway check
No duplicates found among this week's additions in `resources.csv` or
`paid_resources.csv` by name or URL. See "Considered but not added" above for
OpenCode, which is correctly listed in the free/paid pathways already.
||||||| parent of b27e4d0 (viz: add model release timeline (models.html + model_releases.csv))

The whole site now deploys to GitHub Pages at
[chid.github.io/awesome-free-ai](https://chid.github.io/awesome-free-ai/) —
`.github/workflows/pages.yml` publishes the tracked files on every push to
`main`, no build step.

## [2026-09] — Free-list refresh: 7 additions, 1 removal, 6 tier corrections

Snapshot moved from 66 to **72** free resources (66 → 65 after the Amazon Q
removal, +7 new tools). Research verified against official pricing/docs pages on
2026-09-10.

### Added

- **Kiro** (Code Assistant) — AWS's agentic IDE and the official replacement for
  Amazon Q Developer; free $0 plan with monthly credits
- **Hermes Agent** (Agent Framework) — Nous Research's MIT-licensed self-improving
  personal agent with persistent memory and automatic skill creation
- **Multi** (Code Assistant) — free for individual use, BYOK across 100+ models
- **Treblo** (Audio / Music) — unlimited free songs on Melodia v3 (formerly Sonauto)
- **Fish Audio** (Audio / Voice) — 8,000 credits/month free + free flagship API
  (flagged by the vendor as "initial period"; watch for tightening)
- **m_flow** (RAG Framework) — Apache-2.0 cognitive-memory / Graph-RAG engine
- **Matilda (Maincode)** (Code Assistant) — Maincode's Australian sovereign-AI
  coding agent (terminal CLI + desktop app); free during Public Beta

### Removed

- **Amazon Q Developer** — free-tier signups blocked since 15 May 2026; end of
  support 30 Apr 2027. Replaced in the list by Kiro.

### Tier corrections (verified 2026-09-10)

- **Google AI Studio** — corrected a wrong note: Gemini 2.5 Pro/Flash endpoints
  were *not* retired June 17 2026 (that was the 2025 release date). Real changes:
  Gemini Pro models left the free tier ~Apr 2026 (free is now Flash/Flash-Lite/Gemma
  only), Google no longer publishes static quota numbers, and unrestricted API keys
  have been blocked since 19 Jun 2026
- **Hugging Face Inference API** — now credits-based: $0.10/month free Inference
  Providers credits instead of open rate-limited access
- **Kling AI** — "66 credits/day" was a misread of the $1=66-credit purchase rate;
  free tier is ~66 credits/month, daily grants now tied to paid plans
- **GitHub Copilot** — the "50 chats/month" figure no longer appears in official
  docs; chat/agent/CLI draw on an unpublished monthly AI Credits allowance
- **OpenRouter** — :free pool grew from 14 to ~18 models (fluctuates); documented
  the 1000/day limit for accounts with $10+ lifetime credit
- **ElevenLabs** — free tier re-denominated from 10k chars/month to 10k
  credits/month usable across TTS, STT, SFX and music

### Checked and unchanged

Windsurf, Cursor, Suno, Cloudflare Workers AI, Cerebras, SambaNova Cloud, Lovable,
Zed, Groq, Mistral La Plateforme. Udio shows conflicting free-tier figures in
third-party sources — left as-is pending an official source.

## [2026-09] — Weekly local refresh: RAG stores, agentic MoE, and new TTS/vision models

60 local tools (was 54). Filled a gap in **Embeddings / RAG** (a self-hosted vector
database alongside the existing embedding server) and added a frontier open-weight
successor model, two new TTS projects, and a new open vision-language model.

### Added
- **GLM-5** (Z.ai) — Frontier-scale MoE model family for agentic coding and
  long-horizon engineering, successor generation to GLM-4; GLM-5.3-Flash variant
  runs on a single high-end consumer GPU.
- **Qdrant** — Rust-based, self-hostable vector similarity search engine with
  quantization and on-disk storage; fills the Embeddings / RAG category's
  vector-store gap (the existing entry there is an embedding server, not a store).
- **RAGFlow** — Self-hosted, deep-document RAG engine with agentic retrieval,
  citation grounding, and a built-in agent/workflow layer.
- **Chatterbox** (Resemble AI) — Open-source TTS with emotion control and instant
  voice cloning; Multilingual v3 covers ~25 languages.
- **MOSS-TTS** (OpenMOSS) — Open speech family spanning long-form TTS, dialogue
  synthesis, voice design, sound effects, and realtime streaming, with CPU-only
  and GGUF/ONNX deployment paths.
- **LLaVA-OneVision-2** — Open 8B vision-language model unifying image, long-form
  video, and 3D spatial reasoning in one architecture with a fully released
  training pipeline.

### Edited (drift)
- **GLM-4 / GLM-Edge** and **CogVideoX** — both point to repos under the `THUDM`
  GitHub org, which renamed to `zai-org` (the Zhipu AI / Z.ai rebrand). Updated
  both URLs to the new org; content, license, and category are unchanged.

### Cross-pathway check
No duplicates found — none of this week's additions appear in `resources.csv` or
`paid_resources.csv` by name or URL.

## [2026-09] — Weekly local refresh: benchmarking & on-device TTS

54 local tools (was 50). Filled the previously-empty **Hardware / Benchmarking** category and added a CPU-only on-device TTS model. Also normalized `local_resources.csv` and `local_history.csv` to LF line endings and removed a stray mid-file blank row and trailing blank lines that had crept in from earlier edits — no content changed.

### Added
- **TokenSpeed** (LightSeek) — Agentic LLM inference engine separating a C++ control-plane state machine from a Python execution plane; targets TensorRT-LLM-class latency with vLLM-like usability on datacenter GPUs.
- **Atomic Chat** — Offline-first desktop/mobile LLM chat app with a Hugging Face model browser and local OpenAI-compatible server; began as a fork of Jan and has since diverged into its own engine and roadmap.
- **LocalScore** (Mozilla Builders) — Open-source CLI benchmark, built on llamafile, that measures local LLM throughput/latency on your own hardware against a public leaderboard.
- **NeuTTS Air** (Neuphonic) — 748M-parameter on-device text-to-speech model with 3-second voice cloning that runs in real time on CPU alone.

### Flagged for follow-up (not changed here)
- `resources.csv` still lists **Ollama**, **LM Studio**, **Jan**, **GPT4All**, and **Stable Diffusion (via DiffusionBee)** under its "Local / Self-hosted" / "Image Generation" categories at the exact same URLs as their `local_resources.csv` entries — a one-tool-two-pathways duplication, not a freemium pair. Recommend removing these five rows from `resources.csv` since each runs entirely on the reader's own hardware.
- **GPT4All**'s last commit is May 27, 2025 (15+ months stale) with multiple unanswered "is this dead?" issues, though the repo is not formally archived — worth a manual look before citing it as actively maintained.
- The local-tool category taxonomy in current use (`Open Weights (LLM)`, `Vision & Multimodal`, `Image & Video Gen`, `Audio & Speech`, `Evaluation & Harnesses`) has drifted from the list documented in `CLAUDE.md` / `local_refresh_prompt.md` (`Image / Audio / Video`, no model/vision/eval categories at all). This refresh followed the categories already established in the data for consistency; recommend reconciling the docs with reality.

## [2026-09] — AI Agent & Coding Harnesses addition

50 local tools (was 37). Added dedicated tracking for both **Autonomous Coding Agent Harnesses** (modular terminal runtimes turning LLMs into software engineers) and **Evaluation & Benchmark Harnesses**.

### Added (Coding & Agent Execution Harnesses)
- **Pi** (earendil-works) — Minimalist, modular terminal-first AI coding agent harness with read/write/edit/bash primitives and TypeScript extension ecosystem.
- **Codebuff** — Open-source terminal-first AI coding agent harness coordinating a team of specialized sub-agents (explorer, planner, editor, reviewer).
- **Goose** (Block / Linux Foundation AAIF) — Extensible open-source autonomous developer agent harness with tool orchestration and Model Context Protocol (MCP).
- **Plandex** — Terminal AI agent harness for complex multi-file development with 2M+ token context indexing and branch-based plan sandboxes.
- **SWE-agent** (Princeton) — Open-source agent harness turning LLMs into autonomous software engineers to solve real GitHub issues via Agent-Computer Interfaces (ACI).
- **Roo Code** — Open-source autonomous coding agent harness for VS Code with custom role modes (Architect, Code, Ask, Debug) and MCP servers.

### Added (Evaluation & Benchmark Harnesses)
- **lm-evaluation-harness** (EleutherAI) — Standard framework for few-shot evaluation across 60+ benchmarks (MMLU, GSM8K, ARC, HumanEval) powering the Open LLM Leaderboard.
- **SWE-bench** (Princeton) — Industry benchmark and evaluation harness for autonomous coding agents against real GitHub issues in Docker sandboxes.
- **Inspect AI** (UK AI Safety Institute) — Open-source evaluation framework for LLM capabilities, agent tool-use protocols, and sandboxed safety evaluations.
- **Promptfoo** — CLI and CI/CD test harness for testing LLM outputs, prompt assertions, red-teaming, and regression suites.
- **DeepEval** (Confident AI) — Production unit testing framework for LLMs (Pytest for AI) covering hallucination, answer relevancy, and G-Eval.
- **Ragas** — Evaluation harness tailored for Retrieval-Augmented Generation (RAG) pipelines (faithfulness, context recall and precision).
- **Lighteval** (Hugging Face) — Lightweight evaluation toolkit for assessing LLMs across multi-turn chat, math, and custom evaluation suites.


---

## [2026-09] — Paid subscriptions expansion


27 paid resources (was 6). Broadened paid tools tracking across frontier chatbots, AI coding IDEs, generative video, music/voice synthesizers, and enterprise productivity subscriptions.

### Added
- **Frontier LLM Subscriptions**:
  - **ChatGPT Plus / Pro** ($20 / $200/mo) — GPT-4o, o1, o3-mini reasoning, Deep Research, and Advanced Voice.
  - **Claude Pro / Team** ($20 / $25-30/mo) — Claude 3.7 Sonnet hybrid extended thinking, Artifacts, and Projects.
  - **Gemini Advanced** ($19.99/mo) — Google One AI Premium with Gemini 2.0/1.5 Pro (2M context) and Workspace apps.
  - **Grok / X Premium+** ($16-$22/mo) — Real-time X grounding, Grok 3 reasoning, Aurora thinking mode, FLUX image gen.
  - **Perplexity Pro** ($20/mo) — Unlimited Pro Search with multi-model switching (Claude 3.7, GPT-4o, DeepSeek R1).
- **Code Assistants & IDEs**:
  - **Cursor Pro** ($20/mo) — 500 fast requests/mo, Agent Composer, and predictive Cursor Tab.
  - **Windsurf Pro** ($15-$20/mo) — Unlimited Cascade Flow actions with daily/weekly quotas and Claude 3.7.
  - **GitHub Copilot Pro** ($10/mo) — Multi-model switching across Claude 3.7 Sonnet, GPT-4o, and Gemini 2.0 Flash.
  - **Augment Code** ($20/user/mo) — Enterprise codebase instant context understanding and pair programming.
- **Media Generation (Video, Music, Voice, Image)**:
  - **Runway** ($12-$76/mo) — Gen-3 Alpha, Act-One motion capture, and camera control.
  - **Luma Dream Machine** ($29.99-$99.99/mo) — High-fidelity text/image-to-video with camera keyframes.
  - **Pika Pro** ($10-$60/mo) — Pikaffects (melt, inflate, crush), lip sync, and sound effects.
  - **ElevenLabs** ($5-$99/mo) — Ultra-realistic voice cloning, multilingual dubbing, and speech-to-speech.
  - **Suno** ($10-$30/mo) — Radio-ready vocal song generation with full commercial terms.
  - **Udio** ($10-$30/mo) — High-fidelity music generation with stem separation and audio inpainting.
  - **Magnific AI** ($39-$299/mo) — AI image upscaler and hallucination enhancer for photorealistic detail.
- **Enterprise & Productivity**:
  - **Microsoft Copilot Pro** ($20/mo) — GPT-4o integration inside Word, Excel, PowerPoint, and Outlook.
  - **Descript** ($12-$24/user/mo) — Text-based audio and video editing with Studio Sound.
  - **Granola** ($10/user/mo) — AI notepad for meetings with automated transcription and template summaries.
  - **Glean** (~$30-$50/user/mo) — Enterprise work search across Google Workspace, Slack, Jira, and GitHub.
  - **Gamma** ($10-$20/user/mo) — Generative AI canvas for presentations, documents, and webpages.

---

## [2026-08] — Local LLM tools refresh


18 local/self-hosted tools (was 12).

### Added

Fills four previously-empty local categories:

- **OpenHands** (Code Assistant) — self-hosted autonomous coding agent (formerly OpenDevin), MIT, sandboxed Docker execution via CLI or web GUI.
- **AnythingLLM** (Web UI) — all-in-one self-hosted RAG + no-code agents + multi-model chat, MIT.
- **Unsloth** (Fine-tuning / Quant) — fast local LoRA/QLoRA fine-tuning with a no-code Studio UI, Apache-2.0 core.
- **Text Embeddings Inference** (Embeddings / RAG) — Hugging Face's self-hosted embedding/reranking server, Apache-2.0.
- **ComfyUI** (Image / Audio / Video) — node-based local diffusion UI for Stable Diffusion/Flux, GPL-3.0.
- **LocalAGI** (Agent Framework) — self-hostable agent orchestration platform from the LocalAI team, MIT.

### Changed (drift)

- **ExLlamaV2 → ExLlamaV3** — ExLlamaV2 was archived by its maintainer in March 2026; development continues on ExLlamaV3 (new EXL3 quant format, same MIT license).
- **Text Generation WebUI → TextGen (oobabooga)** — project renamed and repo moved to `oobabooga/textgen` in 2026, now ships a native Electron desktop app and an OpenAI/Anthropic-compatible API; license unchanged (AGPL-3.0).

## [2026-09-05] — Pathway cleanup

Five tools were listed twice, once in the free list and once in the local list. The free
list's `Local / Self-hosted` category had been doing the job `local_resources.csv` now does
properly, with hardware requirements and licences per tool.

That category is retired. Ollama, LM Studio, Jan, GPT4All and Stable Diffusion (via
DiffusionBee, listed there as `DiffusionBee`) were removed from `resources.csv`; all five
were already present in the local pathway, so nothing was lost. Free resources drop
71 → 66, and no tool is now listed in more than one pathway.

Counts in `README.md` were also stale and have been corrected to 66 free, 50 local,
28 paid.

Freemium pairs such as `Claude (Anthropic)` / `Claude Pro / Team / Max` are untouched —
a free tier and a separately-named paid plan are intended to coexist.

---

## [2026-08] — August 2026 refresh

71 free resources (was 65), 6 paid (was 0).

### Added

**LLM APIs** — the free-inference field widened considerably since May.

- **Cloudflare Workers AI** — serverless GPU inference at the edge; 10,000 Neurons/day, resetting at 00:00 UTC.
- **SambaNova Cloud** — 200,000 tokens/day per model on RDU hardware.
- **NVIDIA NIM** — OpenAI-compatible endpoints for 120+ open-weight models; 1,000 free credits at ~40 req/min.

**Routers & Clients**

- **Vercel AI Gateway** — one endpoint to 200+ models across 40+ providers; $5 of credit per month, refreshing.

**Code Assistants** — the BYOK agent category consolidated around a few open-source projects.

- **Cline** — MIT-licensed VS Code agent; the project most other VS Code agents were forked from.
- **Kilo Code** — VS Code / JetBrains / CLI / Slack agent with 500+ models at zero inference markup. Now on `kilo.ai`.
- **Zed** — Rust editor with native AI and MCP support; free Personal plan includes 2,000 edit predictions/month.

**Video Generation**

- **Dreamina (Seedance 2.0)** — ByteDance's video model with native audio; daily free credits, up to 1080p, watermark-free.

**Local LLMs pathway** — created `local_resources.csv` (12 seed tools: Ollama, llama.cpp, LM Studio, Jan, vLLM, SGLang, Open WebUI, Kobold.cpp, ExLlamaV2, Text Generation WebUI, LocalAI, Tabby), tracked via `local_history.csv` and refreshed via `local_refresh_prompt.md`. The web page gained a dedicated "Run It Yourself" section below the main grid, showing each tool's category, hardware requirements, and licence. Local tools are counted separately and stay out of the Free/Paid/All totals so month-on-month counts remain comparable. The refresh scope also covers local embeddings/RAG, image/audio/video runners, and hardware/benchmarking tools.

**Paid list** — `paid_resources.csv` was empty at the start of the month; it now holds 6 entries.

- **Midjourney** — $10/mo Basic through $120/mo Mega. No free tier or trial since March 2023.
- **OpenCode Go** — $5 first month then $10/mo for 18 hosted open coding models via OpenCode Zen. The
  open-source OpenCode agent itself is unaffected and stays on the free list.
- **Tabnine** — $39/user/mo Code Assistant, $59/user/mo Agentic Platform, billed annually. The Basic plan was
  retired in 2025; only a 14-day trial remains. Sells privacy, not price — self-hosted, VPC and air-gapped
  deployment, no training or retention on your code.
- **Superhuman** — from $25/user/mo annually ($30 monthly), Business $40. No free tier. Acquired by Grammarly
  in 2025.
- **Sudowrite** — $10–$44/mo annually ($19–$59 monthly). One-time ~10,000-credit trial, no ongoing free plan.

### Moved — free list to paid list

- **Notion AI** — the Free plan gets a capped AI *trial*, not the assistant. Real access starts at Notion Plus
  ($10/user/mo, basic writing) or Business ($20/user/mo, agents). It was carrying a vague
  `Free trial; requires Notion plan` tier value that the inclusion criteria don't allow, so it moved to
  `paid_resources.csv` — logged as `remove` in `history.csv` and `add` in `paid_history.csv`.

**Notes**

- **ChatGPT policy** — logged OpenAI's commitment that the core ChatGPT chat tier remains permanently free (with rate limits on new frontier models).
- **[`QUOTAS.md`](QUOTAS.md)** — new. Tracks how paid AI plans meter usage rather than what they charge:
  the 2026 move off flat-rate, a dated timeline of every limit change, and a per-tool table of Claude Code,
  ChatGPT/Codex, Copilot, Cursor, Windsurf and OpenCode Go. Prices barely moved this year; the unit
  underneath them changed completely.


### Removed

- **Gemini CLI** — stopped serving requests for free, AI Pro and Ultra personal accounts on **18 June 2026**.
  Google's replacement is Antigravity CLI (`agy`), covered by the existing **Antigravity** entry. Enterprise
  licences via Gemini Code Assist Standard/Enterprise are unaffected.

### Changed — free tiers that moved

- **Windsurf** — retired the credit system on 19 March 2026. Free plan is now unlimited Tab autocomplete and
  inline edits plus ~25 Cascade Flow Actions/month, on daily/weekly quotas rather than a monthly credit pool.
- **Cursor** — free plan is now branded **Hobby**: limited Agent requests and Tab completions, no credit card.
  The one-year free student Pro program ended in 2026.
- **Suno** — audio downloads were removed from the free tier in January 2026 after the Warner Music settlement.
  Free tracks stream and share on Suno but can't be downloaded or monetised. Still 50 credits/day (~10 songs).
- **Udio** — settled with Universal Music on similar terms; free tier is now 10 songs/month.
- **OpenRouter** — free tier pinned down: 14 models at ~50 requests/day, up to 1M context.
- **Cohere** — trial key is 1,000 calls/month and **non-commercial use only**.
- **Groq** — free tier is ~30 requests/min on open models.
- **Google AI Studio** — the Gemini 2.5 Pro/Flash endpoint retirement (17 June 2026) has taken effect. Current
  Flash models remain free with no credit card.
- **Antigravity** — now the official Gemini CLI replacement, shipping both the IDE and the `agy` CLI.
- **GitHub Copilot** — free tier is unchanged at 2,000 completions + 50 chats/month, but paid plans moved to
  token-based **AI Credits** on 1 June 2026. Inline completions and next-edit suggestions never draw down the
  balance; chat, agent mode, code review and the CLI do.
- **OpenCode** — description now mentions the optional paid Go plan. The agent stays free, open-source and BYOK.

### Fixed

- Three rows (`MetaGPT`, `models.dev`, `Freebuff`) had descriptions containing unquoted commas, which shifted
  every field after the description and rendered the wrong text as `free_tier` and `requires_signup` in both the
  web view and any CSV reader. Descriptions are now quoted.
- `README.md` was several refreshes behind `resources.csv` — it listed 63 tools and was missing every entry added
  on 16 and 23 May. It is now regenerated from the CSV and covers all 72, with new **Routers & Clients** and
  **Frameworks** sections for the categories that had no home.

---

## [2026-05] — May 2026

Initial release and two follow-up passes. 65 free resources at close of month.

### Added

- **15 May** — initial 40-resource seed, then a research refresh adding Cerebras, Le Chat, DeepSeek, Gemini CLI,
  Amazon Q Developer, Kling AI and Pika.
- **16 May** — developer tooling: LiteLLM, LangChain, LlamaIndex, DSPy, aisuite. Paid-tools tracking initialised.
- **23 May** — agent frameworks (CrewAI, AutoGen, MetaGPT, AgentScope), free DeepSeek access (Chutes.ai,
  Puter.js), terminal agents (Freebuff, OpenCode), Lovable, and Muse Spark — Meta Superintelligence Labs' first
  natively multimodal model, free via meta.ai. Antigravity added as Google's incoming Gemini CLI replacement.

### Changed

- **GitHub Copilot** — free for all users (2,000 completions + 50 chats/month), no longer students-only.
- **Codeium → Windsurf** — rebranded; name, URL, description and tier all updated.
- **OpenRouter** — corrected: the `:free` suffix is a rate-limited community tier, not permanently free models.
- **Gemini CLI / Google AI Studio** — flagged the June 2026 deprecations ahead of time.

### Removed

- Frontier model pricing and context-window tracking, in favour of linking to [models.dev](https://models.dev).
