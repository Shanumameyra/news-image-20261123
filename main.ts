// Entry program for news-image-20261123.
// Copies the pre-drawn front page (entry.png, made by draw_image.py)
// into the grader's output directory. Pure Node standard library,
// no network, fully deterministic: the same bytes every run.
import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });
copyFileSync(join(here, "entry.png"), join(outDir, "entry.png"));
