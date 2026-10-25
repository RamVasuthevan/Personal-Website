// Live Python console examples for posts.
//
// In a post's Markdown, write the lines to type in a code fence tagged `repl`.
// Only the input is written; the output comes from running it.
//
//   ```repl
//   from collections import Counter
//   C = Counter(["Partridge", "Turtle Dove", "Turtle Dove"])
//   C.items()
//   ```
//
// Each such fence is rebuilt as a console block (styled in main.scss) with a
// button that copies its input lines. Python is then loaded in the browser
// (Pyodide) and every block on the page is run in order in one shared session,
// showing the output and leaving a prompt readers can keep typing at.
//
// As in a real Python prompt, a statement with an indented body (for, if, def)
// must be followed by a blank line.

// To upgrade Python, change the version in this URL.
const PYODIDE_URL = "https://cdn.jsdelivr.net/pyodide/v314.0.7/full/pyodide.mjs";

// Python that sets up the session. It evaluates to run(line), which feeds one
// line to an interactive console and returns what that printed, or None when
// the statement is not finished and needs more lines.
const PYTHON_SESSION = `
from pyodide.console import PyodideConsole

printed = []
console = PyodideConsole(stdout_callback=printed.append, stderr_callback=printed.append)

async def run(line):
    printed.clear()
    result = console.push(line)
    if result.syntax_check == "incomplete":
        return None
    try:
        value = await result
        if value is not None:
            printed.append(repr(value))
    except BaseException:  # also exit() and the like, which must not break the page
        printed.append(result.formatted_error)
    return "".join(printed).rstrip()

run
`;

// Icons for the copy button: two overlapping sheets, and a tick once copied.
const ICON = (shape) =>
  `<svg viewBox="0 0 16 16" width="16" height="16" fill="none" stroke="currentColor" stroke-width="1.5">${shape}</svg>`;
const COPY_ICON = ICON(
  '<rect x="5.5" y="5.5" width="8" height="8" rx="1.5"/><path d="M10.5 5.5v-2a1 1 0 0 0-1-1h-6a1 1 0 0 0-1 1v6a1 1 0 0 0 1 1h2"/>'
);
const COPIED_ICON = ICON('<path d="M3 8.5l3.5 3.5L13 4.5"/>');

const blocks = buildConsoleBlocks();
if (blocks.length > 0) goLive(blocks);

// Replaces each `repl` code fence with a console block and returns the blocks.
function buildConsoleBlocks() {
  const blocks = [];

  for (const source of document.querySelectorAll(".post-content code")) {
    // Jekyll marks the fence on <code> inside a list, and on a wrapper elsewhere.
    const fence = source.closest("div.language-repl") ?? source.closest("pre:has(> .language-repl)");
    if (!fence) continue;
    const lines = source.textContent.trimEnd().split("\n");

    const code = document.createElement("code");
    code.append(...lines.map((line) => span("repl-input", line)));
    code.append(span("repl-input repl-waiting", ""));

    const pre = document.createElement("pre");
    pre.append(code);
    const block = document.createElement("div");
    block.className = "repl";
    block.append(copyButton(code), pre);
    fence.replaceWith(block);
    blocks.push(block);
  }

  return blocks;
}

// Makes a button that copies a block's input lines, without prompts or output.
function copyButton(code) {
  const button = document.createElement("button");
  button.className = "repl-copy";
  button.ariaLabel = "Copy code";
  button.title = "Copy code";
  button.innerHTML = COPY_ICON;

  button.addEventListener("click", async () => {
    // Skip the waiting line and the line the reader is still typing.
    const lines = code.querySelectorAll(".repl-input:not(.repl-waiting):not(:has(input))");
    const text = [...lines].map((line) => line.textContent).join("\n");
    await navigator.clipboard.writeText(text);

    button.innerHTML = COPIED_ICON;
    setTimeout(() => (button.innerHTML = COPY_ICON), 1500);
  });

  return button;
}

// Loads Python, then runs every block in order and gives each a prompt the
// reader can type at. If Python cannot be loaded, the blocks show only their
// input lines.
async function goLive(blocks) {
  blocks.forEach((block) => block.classList.add("repl-loading"));

  try {
    const { loadPyodide } = await import(PYODIDE_URL);
    const pyodide = await loadPyodide();
    const run = pyodide.runPython(PYTHON_SESSION);

    for (const block of blocks) {
      block.querySelector(".repl-waiting").remove();

      let isContinuation = false;
      for (const line of block.querySelectorAll(".repl-input")) {
        line.classList.toggle("repl-continued", isContinuation);
        isContinuation = await runLine(line, run);
      }
      addPrompt(block, run, isContinuation);
    }
  } catch (error) {
    console.warn("Python console examples are not live:", error);
  }

  blocks.forEach((block) => block.classList.remove("repl-loading"));
}

// Runs one input line and shows what it printed underneath. Returns whether the
// statement is unfinished, meaning the next line continues it.
async function runLine(line, run) {
  const output = await run(line.textContent);
  if (output) line.after(span("repl-output", output));
  return output === undefined;
}

// Adds a prompt line with a text field to the end of a block and returns the
// field. Pressing Enter runs what was typed and adds the next prompt.
function addPrompt(block, run, isContinuation) {
  const line = span("repl-input", "");
  line.classList.toggle("repl-continued", isContinuation);

  const field = document.createElement("input");
  field.ariaLabel = "Python input";
  field.autocapitalize = "off";
  field.autocomplete = "off";
  field.spellcheck = false;

  field.addEventListener("keydown", async (event) => {
    if (event.key !== "Enter") return;

    line.textContent = field.value; // the field gives way to the text that was typed
    const isUnfinished = await runLine(line, run);
    addPrompt(block, run, isUnfinished).focus();
  });

  line.append(field);
  block.querySelector("code").append(line);
  return field;
}

function span(className, text) {
  const element = document.createElement("span");
  element.className = className;
  element.textContent = text;
  return element;
}
