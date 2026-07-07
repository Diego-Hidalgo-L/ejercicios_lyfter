import { useState } from "react";

const questions = [
  // ── SECTION 1: Programming Languages ──
  {
    section: "Programming Languages",
    emoji: "🖥️",
    type: "multiple",
    question: "A compiled language translates code...",
    options: [
      "Line by line, as it runs",
      "All at once, before execution",
      "Only when there are no errors",
      "Using a virtual machine at runtime",
    ],
    answer: 1,
    explanation:
      "Compiled languages translate the entire program into machine code before running it, making them faster but less forgiving with errors found only at compile time.",
  },
  {
    section: "Programming Languages",
    emoji: "🖥️",
    type: "multiple",
    question:
      "Which of these is a key trade-off of interpreted languages like Python?",
    options: [
      "They're harder to write but much faster",
      "They require explicit type declarations",
      "Errors deep in the code only appear when execution reaches them",
      "They must be compiled before every run",
    ],
    answer: 2,
    explanation:
      "Interpreted languages run line by line. A typo on line 500 won't be caught until the program actually reaches it — a classic 'interpreted gotcha'.",
  },
  {
    section: "Programming Languages",
    emoji: "🖥️",
    type: "multiple",
    question: "What does it mean for a language to be 'dynamically typed'?",
    options: [
      "The language compiles faster than statically typed ones",
      "You don't need to declare the type of a variable explicitly",
      "Variables can only hold integer values",
      "The language only runs on dynamic web pages",
    ],
    answer: 1,
    explanation:
      "In dynamically typed languages like Python, you just write `x = 5` and Python figures out the type. In statically typed ones you'd write `int x = 5`.",
  },

  // ── SECTION 2: Python Data Types ──
  {
    section: "Python — Data Types",
    emoji: "🐍",
    type: "multiple",
    question: "What is the output of the following code?\n\nprint(type(3.14))",
    options: ["<class 'int'>", "<class 'number'>", "<class 'float'>", "<class 'decimal'>"],
    answer: 2,
    explanation:
      "3.14 is a decimal number, so its type is `float`. Remember: int = whole numbers, float = decimals.",
  },
  {
    section: "Python — Data Types",
    emoji: "🐍",
    type: "multiple",
    question:
      "You have a list `data = ['a', 'b', 'c', 'd']`. What does `data[2]` return?",
    options: ["'b'", "'c'", "'d'", "IndexError"],
    answer: 1,
    explanation:
      "List indices start at 0. So index 0 = 'a', index 1 = 'b', index 2 = 'c'. Classic off-by-one awareness!",
  },
  {
    section: "Python — Data Types",
    emoji: "🐍",
    type: "multiple",
    question:
      "What is the main difference between a list and a tuple in Python?",
    options: [
      "Lists use () and tuples use []",
      "Tuples are mutable, lists are not",
      "Lists are mutable, tuples are not",
      "They are identical, just different syntax",
    ],
    answer: 2,
    explanation:
      "Lists `[]` can be modified after creation. Tuples `()` are immutable — once created, you can't change their elements.",
  },
  {
    section: "Python — Data Types",
    emoji: "🐍",
    type: "short",
    question:
      "What will the following print?\n\nmy_dict = {'name': 'Ada', 'age': 36}\nprint(my_dict.get('email'))",
    answer: "None",
    explanation:
      "`.get()` returns `None` (not an error) when a key doesn't exist. This is safer than `my_dict['email']` which would throw a KeyError.",
  },

  // ── SECTION 3: Iterations ──
  {
    section: "Python — Iterations",
    emoji: "🔁",
    type: "multiple",
    question:
      "When should you prefer a `while` loop over a `for` loop?",
    options: [
      "When you know exactly how many times to iterate",
      "When iterating over a list",
      "When you don't know how many times the loop should run",
      "`while` loops are always better than `for` loops",
    ],
    answer: 2,
    explanation:
      "`for` loops shine when you have a defined iterable. `while` loops are your go-to when the stopping condition depends on something dynamic that changes during execution.",
  },
  {
    section: "Python — Iterations",
    emoji: "🔁",
    type: "multiple",
    question:
      "What is the output of this snippet?\n\ncolors = ['red', 'blue', 'green']\nfor i, c in enumerate(colors):\n    print(i, c)",
    options: [
      "red blue green",
      "0 red\n1 blue\n2 green",
      "1 red\n2 blue\n3 green",
      "An error — enumerate needs two separate variables",
    ],
    answer: 1,
    explanation:
      "`enumerate()` gives you index + value pairs. Indices start at 0. It's the elegant alternative to manually tracking an index variable.",
  },
  {
    section: "Python — Iterations",
    emoji: "🔁",
    type: "multiple",
    question:
      "What does `continue` do inside a loop?",
    options: [
      "Stops the loop entirely",
      "Restarts the entire program",
      "Skips the rest of the current iteration and moves to the next one",
      "Jumps to the outermost loop",
    ],
    answer: 2,
    explanation:
      "`continue` skips what's left in the current loop iteration. `break` stops the loop entirely. Don't mix these up in an interview!",
  },

  // ── SECTION 4: Exceptions ──
  {
    section: "Python — Exceptions",
    emoji: "🚨",
    type: "multiple",
    question:
      "What exception does this code raise?\n\nmy_list = [1, 2, 3]\nprint(my_list[5])",
    options: ["ValueError", "TypeError", "IndexError", "KeyError"],
    answer: 2,
    explanation:
      "`IndexError` is raised when you try to access a list index that doesn't exist. `KeyError` is for dicts, `ValueError` for bad value conversions.",
  },
  {
    section: "Python — Exceptions",
    emoji: "🚨",
    type: "multiple",
    question:
      "What is considered a BAD practice with try/except?",
    options: [
      "Using multiple except blocks for different error types",
      "Using the except block for the 'happy path' logic",
      "Wrapping risky operations in try/except",
      "Catching specific exception types like ValueError",
    ],
    answer: 1,
    explanation:
      "The `except` block is for error handling — not your normal flow. Putting happy-path code inside `except` is a code smell that can get you fired. True story.",
  },
  {
    section: "Python — Exceptions",
    emoji: "🚨",
    type: "code",
    question:
      "Fix the bug: the following code crashes because a variable is declared inside `try`. Rewrite it correctly.\n\ntry:\n    result = int('hello')\nexcept ValueError:\n    print('Bad input')\n\nprint(result)",
    answer:
      "result = 0\ntry:\n    result = int('hello')\nexcept ValueError:\n    print('Bad input')\n\nprint(result)",
    explanation:
      "Declare `result` with a placeholder value BEFORE the try block. If the try fails, `result` still exists as its placeholder, avoiding a NameError.",
  },

  // ── SECTION 5: Scope ──
  {
    section: "Python — Scope",
    emoji: "🔭",
    type: "multiple",
    question:
      "What happens when you try to access a variable declared inside a function from outside it?",
    options: [
      "It works fine, variables are always global",
      "You get a NameError because the variable doesn't exist outside its local scope",
      "Python automatically makes it global",
      "It returns None",
    ],
    answer: 1,
    explanation:
      "Variables inside a function live in the function's local scope. Once the function ends, they're gone. They don't exist outside their scope.",
  },
  {
    section: "Python — Scope",
    emoji: "🔭",
    type: "multiple",
    question:
      "Why are global variables considered bad practice for mutable data?",
    options: [
      "They use more memory than local variables",
      "Python doesn't allow global variables",
      "Multiple functions can modify them, making it hard to trace where changes happen",
      "They are automatically deleted after each function call",
    ],
    answer: 2,
    explanation:
      "If 7 functions all modify a global list, good luck debugging which one caused the problem. Pass data via parameters and returns instead.",
  },

  // ── SECTION 6: File Handling ──
  {
    section: "Python — File Handling",
    emoji: "📁",
    type: "multiple",
    question:
      "What is the difference between opening a file with mode `'a'` vs mode `'w'`?",
    options: [
      "'a' overwrites the file; 'w' appends to it",
      "'a' appends to existing content; 'w' overwrites (or creates) the file",
      "They are identical",
      "'a' is for reading; 'w' is for writing",
    ],
    answer: 1,
    explanation:
      "`'w'` = write mode: wipes the file and starts fresh. `'a'` = append mode: adds to the end without destroying what's there.",
  },
  {
    section: "Python — File Handling",
    emoji: "📁",
    type: "multiple",
    question: "Why is it recommended to use `with open(...) as file:` instead of just `open(...)`?",
    options: [
      "It's faster",
      "It automatically closes the file and frees resources when the block ends",
      "It's required for reading CSV files",
      "It prevents encoding errors",
    ],
    answer: 1,
    explanation:
      "`with` guarantees the file is closed after the block, even if an error occurs. Forgetting to close files can cause memory leaks and lock files for other processes.",
  },

  // ── SECTION 7: Infinite Params ──
  {
    section: "Python — Infinite Params",
    emoji: "♾️",
    type: "multiple",
    question:
      "What is the difference between `*args` and `**kwargs`?",
    options: [
      "`*args` collects named keyword arguments; `**kwargs` collects positional ones",
      "`*args` collects positional arguments as a list; `**kwargs` collects named arguments as a dict",
      "They are interchangeable",
      "`*args` is for strings only; `**kwargs` is for numbers",
    ],
    answer: 1,
    explanation:
      "`*args` → positional args → comes in as a tuple/list. `**kwargs` → keyword args (name=value) → comes in as a dict. Order: regular params, then *args, then **kwargs.",
  },
  {
    section: "Python — Infinite Params",
    emoji: "♾️",
    type: "short",
    question:
      "What will this print?\n\ndef greet(*args):\n    for name in args:\n        print(f'Hello {name}')\n\ngreet('Alice', 'Bob', 'Carol')",
    answer: "Hello Alice\nHello Bob\nHello Carol",
    explanation:
      "`*args` captures all positional arguments into a tuple. The loop iterates over them and prints each greeting.",
  },

  // ── SECTION 8: Decorators ──
  {
    section: "Python — Decorators",
    emoji: "🎀",
    type: "multiple",
    question: "What does a decorator fundamentally do?",
    options: [
      "It changes the name of a function",
      "It wraps a function to add behavior before and/or after it runs",
      "It converts a function into a class method",
      "It makes a function run faster",
    ],
    answer: 1,
    explanation:
      "A decorator is a function that takes another function and returns a new one with extra behavior. They follow the DRY principle by centralizing cross-cutting concerns like auth checks.",
  },
  {
    section: "Python — Decorators",
    emoji: "🎀",
    type: "multiple",
    question: "Which built-in decorator lets you call a method like an attribute (no parentheses)?",
    options: ["@classmethod", "@staticmethod", "@property", "@abstractmethod"],
    answer: 2,
    explanation:
      "`@property` lets you define a method that behaves like an attribute — great for computed values like `age` calculated from `date_of_birth`. No `()` needed when accessing it.",
  },

  // ── SECTION 9: OOP ──
  {
    section: "OOP — Concepts",
    emoji: "🏗️",
    type: "multiple",
    question: "What is the correct relationship between a class and an object?",
    options: [
      "A class is an instance of an object",
      "An object is an instance of a class",
      "They are the same thing",
      "A class can only have one object",
    ],
    answer: 1,
    explanation:
      "A class is the blueprint/mold. An object is what you create FROM that blueprint. One class → infinite possible objects.",
  },
  {
    section: "OOP — Concepts",
    emoji: "🏗️",
    type: "multiple",
    question: "In Python, what is `__init__`?",
    options: [
      "A method that destroys an object",
      "The constructor — it runs automatically when an object is instantiated",
      "A private attribute",
      "A static method available on all classes",
    ],
    answer: 1,
    explanation:
      "`__init__` is the constructor. It's called automatically when you do `MyClass()`. Use it to set up initial attributes and run setup logic.",
  },
  {
    section: "OOP — Concepts",
    emoji: "🏗️",
    type: "multiple",
    question: "What does `self` refer to inside a method?",
    options: [
      "The class itself",
      "The parent class",
      "The specific object instance that called the method",
      "A global variable",
    ],
    answer: 2,
    explanation:
      "`self` refers to the specific instance calling the method. That's how `my_car.upgrade_engine()` knows to modify `my_car`'s data and not `my_truck`'s.",
  },
  {
    section: "OOP — Four Pillars",
    emoji: "🏛️",
    type: "multiple",
    question: "Which OOP pillar does this code demonstrate?\n\nclass Car(Vehicle):\n    wheel_number = 4",
    options: ["Encapsulation", "Polymorphism", "Inheritance", "Abstraction"],
    answer: 2,
    explanation:
      "`Car` inheriting from `Vehicle` is classic inheritance. The child class gets all the attributes and methods of the parent class.",
  },
  {
    section: "OOP — Four Pillars",
    emoji: "🏛️",
    type: "multiple",
    question: "Polymorphism in OOP means...",
    options: [
      "A class can only have one shape",
      "Methods with the same name can behave differently depending on the object",
      "All classes must inherit from a base class",
      "Private methods cannot be overridden",
    ],
    answer: 1,
    explanation:
      "Poly = many, morph = forms. `encender()` on a `Vehiculo` turns on the engine; on a `Computadora` it boots the OS. Same name, different behavior.",
  },
  {
    section: "OOP — Four Pillars",
    emoji: "🏛️",
    type: "multiple",
    question: "In Python's encapsulation convention, what does a double underscore prefix (`__attribute`) signal?",
    options: [
      "The attribute is public",
      "The attribute is protected (accessible by subclasses)",
      "The attribute is intended to be private (internal use only)",
      "The attribute is a class method",
    ],
    answer: 2,
    explanation:
      "Python uses conventions since it lacks true access modifiers. `name` = public, `_name` = protected, `__name` = private. Double underscore is the strongest hint to other devs: hands off!",
  },
  {
    section: "OOP — Four Pillars",
    emoji: "🏛️",
    type: "multiple",
    question: "What makes a class 'abstract' in Python?",
    options: [
      "It has no methods",
      "It inherits from ABC and can have @abstractmethod methods that subclasses MUST implement",
      "It uses only class methods",
      "It cannot have a constructor",
    ],
    answer: 1,
    explanation:
      "An abstract class (inheriting from `ABC`) can't be instantiated directly. Its `@abstractmethod` methods act as contracts: subclasses MUST override them or Python raises an error.",
  },

  // ── SECTION 10: Algorithms ──
  {
    section: "Algorithms — Bubble Sort",
    emoji: "🫧",
    type: "multiple",
    question: "Why is Bubble Sort called 'bubble' sort?",
    options: [
      "It was invented by a developer named Bubble",
      "It uses a bubble data structure internally",
      "Larger values 'bubble up' to the end of the list with each pass",
      "It sorts by popping elements like bubbles",
    ],
    answer: 2,
    explanation:
      "Each pass through the list moves the current largest value toward the end, like bubbles rising to the surface of water. Elegant name, inefficient algorithm.",
  },
  {
    section: "Algorithms — Bubble Sort",
    emoji: "🫧",
    type: "multiple",
    question: "What is the Big O complexity of Bubble Sort?",
    options: ["O(1)", "O(n)", "O(n²)", "O(log n)"],
    answer: 2,
    explanation:
      "Bubble Sort has two nested loops, each running ~n times → O(n²). This is why it's slow for large datasets. Two nested loops = O(n²) is a pattern worth memorizing.",
  },
  {
    section: "Algorithms — Bubble Sort",
    emoji: "🫧",
    type: "multiple",
    question: "The optimized Bubble Sort uses a `has_made_changes` flag. What does this optimization achieve?",
    options: [
      "It reduces memory usage to O(1)",
      "It stops early if no swaps happened in a pass, meaning the list is already sorted",
      "It makes the inner loop run in reverse",
      "It changes the complexity to O(log n)",
    ],
    answer: 1,
    explanation:
      "If a full pass happens with zero swaps, the list is sorted — no need to keep going. This is a great best-case optimization even though worst-case is still O(n²).",
  },
  {
    section: "Algorithms — Big O",
    emoji: "📈",
    type: "multiple",
    question: "What does Big O Notation measure?",
    options: [
      "The exact number of milliseconds an algorithm takes",
      "How much RAM an algorithm uses",
      "The worst-case growth rate of time (or space) relative to input size",
      "The number of lines of code in an algorithm",
    ],
    answer: 2,
    explanation:
      "Big O describes how an algorithm SCALES in the worst case as input grows. It's about the shape of growth, not the exact time.",
  },
  {
    section: "Algorithms — Big O",
    emoji: "📈",
    type: "multiple",
    question: "What is the Big O of this function?\n\ndef find_first(items):\n    return items[0]",
    options: ["O(n)", "O(n²)", "O(log n)", "O(1)"],
    answer: 3,
    explanation:
      "Accessing the first element of a list is always one operation regardless of list size. No loops, no recursion = O(1) constant time.",
  },
  {
    section: "Algorithms — Big O",
    emoji: "📈",
    type: "multiple",
    question: "You have a function with three nested for-loops, each iterating n times. What is its Big O?",
    options: ["O(3n)", "O(n³)", "O(n²)", "O(log n)"],
    answer: 1,
    explanation:
      "Each nested loop multiplies the complexity. 1 loop = O(n), 2 nested = O(n²), 3 nested = O(n³). The 3 in front of n gets dropped in Big O — we only care about the dominant term.",
  },

  // ── SECTION 11: Data Structures ──
  {
    section: "Data Structures — Linked List",
    emoji: "🔗",
    type: "multiple",
    question: "In a Linked List, how do you traverse from the first node to the last?",
    options: [
      "Access them by index like a Python list",
      "Start at `head`, then follow each node's `next` pointer until `next` is None",
      "Use a built-in `.traverse()` method",
      "Access them via a `tail` pointer that points backwards",
    ],
    answer: 1,
    explanation:
      "A Linked List has no random access by index. You start at `head` and hop from node to node via `next` until you hit `None` (the end).",
  },
  {
    section: "Data Structures — Stack & Queue",
    emoji: "📚",
    type: "multiple",
    question: "A Stack is LIFO. What does that mean in practice?",
    options: [
      "The first item added is the first item removed",
      "The last item added is the first item removed",
      "Items are removed randomly",
      "Items are sorted before removal",
    ],
    answer: 1,
    explanation:
      "LIFO = Last In, First Out. Think of a stack of plates — you take from the top, which is the last one placed. `push` adds to top, `pop` removes from top.",
  },
  {
    section: "Data Structures — Stack & Queue",
    emoji: "📚",
    type: "multiple",
    question: "What real-world scenario best models a Queue (FIFO)?",
    options: [
      "A stack of books where you take from the top",
      "A browser's back button history",
      "People lining up at a McDonald's counter",
      "Undo/redo functionality in a text editor",
    ],
    answer: 2,
    explanation:
      "A queue = first person in line gets served first. FIFO = First In, First Out. `enqueue` adds to the back, `dequeue` removes from the front.",
  },
  {
    section: "Data Structures — Deque & Tree",
    emoji: "🌳",
    type: "multiple",
    question: "How does a Double Ended Queue (Deque) differ from a regular Queue?",
    options: [
      "A Deque can only hold two elements",
      "A Deque allows inserting and removing elements from BOTH ends",
      "A Deque is just a Queue with a different name",
      "A Deque stores elements in sorted order",
    ],
    answer: 1,
    explanation:
      "A Deque combines Stack and Queue. It has `push_left`, `push_right`, `pop_left`, `pop_right` — full flexibility at both ends.",
  },
  {
    section: "Data Structures — Deque & Tree",
    emoji: "🌳",
    type: "multiple",
    question: "What distinguishes a Binary Tree node from a Linked List node?",
    options: [
      "A Binary Tree node has a `next` pointer; a Linked List node has `left` and `right`",
      "A Binary Tree node has TWO child pointers (`left` and `right`); a Linked List node has only `next`",
      "They are identical in structure",
      "A Binary Tree node stores only numbers",
    ],
    answer: 1,
    explanation:
      "Linked List nodes point to ONE next node. Binary Tree nodes point to TWO children (left and right). The tree structure enables powerful search and sort algorithms.",
  },
];

const SECTION_COLORS = {
  "Programming Languages": "#00d4ff",
  "Python — Data Types": "#a8ff78",
  "Python — Iterations": "#78ffd6",
  "Python — Exceptions": "#ff6b6b",
  "Python — Scope": "#ffd93d",
  "Python — File Handling": "#c89cff",
  "Python — Infinite Params": "#ff9a56",
  "Python — Decorators": "#ff78c4",
  "OOP — Concepts": "#56cfff",
  "OOP — Four Pillars": "#56ffb8",
  "Algorithms — Bubble Sort": "#ffb347",
  "Algorithms — Big O": "#ff6f91",
  "Data Structures — Linked List": "#b5ead7",
  "Data Structures — Stack & Queue": "#ffd6a5",
  "Data Structures — Deque & Tree": "#caffbf",
};

export default function TechExam() {
  const [current, setCurrent] = useState(0);
  const [answers, setAnswers] = useState({});
  const [submitted, setSubmitted] = useState({});
  const [codeInput, setCodeInput] = useState("");
  const [shortInput, setShortInput] = useState("");
  const [showScore, setShowScore] = useState(false);
  const [revealed, setRevealed] = useState({});

  const q = questions[current];
  const total = questions.length;
  const answeredCount = Object.keys(submitted).length;
  const score = Object.entries(submitted).reduce((acc, [idx]) => {
    const qi = questions[parseInt(idx)];
    const userAns = answers[idx];
    if (qi.type === "multiple" && userAns === qi.answer) return acc + 1;
    if (qi.type === "short" || qi.type === "code") return acc + 1; // self-graded
    return acc;
  }, 0);

  const color = SECTION_COLORS[q.section] || "#00d4ff";
  const isSubmitted = submitted[current] !== undefined;

  function handleMultiple(optIdx) {
    if (isSubmitted) return;
    setAnswers((a) => ({ ...a, [current]: optIdx }));
  }

  function handleSubmit() {
    if (answers[current] === undefined && q.type === "multiple") return;
    const val = q.type === "multiple" ? answers[current] : q.type === "short" ? shortInput : codeInput;
    setAnswers((a) => ({ ...a, [current]: val }));
    setSubmitted((s) => ({ ...s, [current]: true }));
    setRevealed((r) => ({ ...r, [current]: true }));
  }

  function goTo(idx) {
    setCurrent(idx);
    setCodeInput(typeof answers[idx] === "string" ? answers[idx] : "");
    setShortInput(typeof answers[idx] === "string" ? answers[idx] : "");
  }

  const multipleCorrect = q.type === "multiple" && isSubmitted && answers[current] === q.answer;
  const multipleWrong = q.type === "multiple" && isSubmitted && answers[current] !== q.answer;

  if (showScore) {
    const multipleOnly = questions.filter(q => q.type === "multiple");
    const multipleScore = multipleOnly.reduce((acc, qi, i) => {
      const realIdx = questions.indexOf(qi);
      return answers[realIdx] === qi.answer ? acc + 1 : acc;
    }, 0);
    const pct = Math.round((multipleScore / multipleOnly.length) * 100);
    const selfGraded = questions.filter(q => q.type !== "multiple").length;

    return (
      <div style={styles.scoreScreen}>
        <div style={styles.scoreCard}>
          <div style={styles.scoreBig}>{pct}%</div>
          <div style={styles.scoreLabel}>on auto-graded questions</div>
          <div style={styles.scoreSub}>
            {multipleScore} / {multipleOnly.length} multiple choice correct
          </div>
          <div style={styles.scoreSub} className="muted">
            + {selfGraded} short answer / code questions (self-graded)
          </div>
          <div style={styles.scoreBarOuter}>
            <div style={{ ...styles.scoreBarInner, width: `${pct}%` }} />
          </div>
          <div style={styles.scoreMsg}>
            {pct >= 85 ? "🚀 You're absolutely crushing it. Ship it." :
             pct >= 65 ? "💪 Solid foundation. A few gaps to patch." :
             "📚 Back to the notes! You've got the tools."}
          </div>
          <button style={styles.retryBtn} onClick={() => {
            setAnswers({}); setSubmitted({}); setRevealed({});
            setShowScore(false); setCurrent(0);
          }}>
            Retry Exam
          </button>
        </div>
      </div>
    );
  }

  return (
    <div style={styles.root}>
      {/* Header */}
      <div style={styles.header}>
        <div style={styles.headerLeft}>
          <span style={styles.logo}>{'</>'}</span>
          <span style={styles.title}>Tech Interview Exam</span>
        </div>
        <div style={styles.progress}>
          <span style={styles.progNum}>{answeredCount}/{total}</span>
          <div style={styles.progBar}>
            <div style={{ ...styles.progFill, width: `${(answeredCount / total) * 100}%` }} />
          </div>
        </div>
      </div>

      <div style={styles.body}>
        {/* Question Nav Sidebar */}
        <div style={styles.sidebar}>
          {Object.entries(
            questions.reduce((acc, q, i) => {
              if (!acc[q.section]) acc[q.section] = [];
              acc[q.section].push(i);
              return acc;
            }, {})
          ).map(([section, indices]) => (
            <div key={section} style={styles.sideSection}>
              <div style={{ ...styles.sideSectionLabel, color: SECTION_COLORS[section] || "#aaa" }}>
                {section}
              </div>
              <div style={styles.sideNums}>
                {indices.map((i) => (
                  <button
                    key={i}
                    onClick={() => goTo(i)}
                    style={{
                      ...styles.sideNum,
                      background: current === i
                        ? (SECTION_COLORS[questions[i].section] || "#00d4ff")
                        : submitted[i]
                        ? (questions[i].type !== "multiple" || answers[i] === questions[i].answer ? "#1a3a2a" : "#3a1a1a")
                        : "#1a1a2e",
                      color: current === i ? "#000" : submitted[i] ? (questions[i].type !== "multiple" || answers[i] === questions[i].answer ? "#4ade80" : "#f87171") : "#666",
                      border: current === i ? `2px solid ${SECTION_COLORS[questions[i].section] || "#00d4ff"}` : "2px solid #2a2a3e",
                    }}
                  >
                    {i + 1}
                  </button>
                ))}
              </div>
            </div>
          ))}
          <button style={styles.finishBtn} onClick={() => setShowScore(true)}>
            See Results →
          </button>
        </div>

        {/* Main Question Area */}
        <div style={styles.main}>
          <div style={styles.card}>
            {/* Section tag */}
            <div style={{ ...styles.sectionTag, background: color + "22", color }}>
              {q.emoji} {q.section}
            </div>

            {/* Type badge */}
            <div style={styles.typeBadge}>
              {q.type === "multiple" ? "Multiple Choice" : q.type === "short" ? "Short Answer" : "Code Challenge"}
            </div>

            {/* Question */}
            <div style={styles.questionText}>
              {q.question.split("\n").map((line, i) =>
                line.startsWith("    ") || line.match(/^[a-z_]+\s*[=({]/) || line.match(/^\s*(def|class|for|if|print|return|try|except|while)/) ? (
                  <code key={i} style={styles.codeLine}>{line}</code>
                ) : (
                  <span key={i}>{line}<br /></span>
                )
              )}
            </div>

            {/* Multiple choice */}
            {q.type === "multiple" && (
              <div style={styles.options}>
                {q.options.map((opt, i) => {
                  let bg = "#1a1a2e";
                  let border = "#2a2a4e";
                  let textColor = "#ccc";
                  if (answers[current] === i && !isSubmitted) { bg = "#1e2a4a"; border = color; textColor = "#fff"; }
                  if (isSubmitted && i === q.answer) { bg = "#0a2a0a"; border = "#4ade80"; textColor = "#4ade80"; }
                  if (isSubmitted && answers[current] === i && i !== q.answer) { bg = "#2a0a0a"; border = "#f87171"; textColor = "#f87171"; }
                  return (
                    <button key={i} style={{ ...styles.option, background: bg, border: `2px solid ${border}`, color: textColor }}
                      onClick={() => handleMultiple(i)}>
                      <span style={styles.optLetter}>{String.fromCharCode(65 + i)}</span>
                      {opt}
                    </button>
                  );
                })}
              </div>
            )}

            {/* Short answer */}
            {q.type === "short" && (
              <div style={styles.shortArea}>
                <input
                  style={styles.shortInput}
                  placeholder="Type your answer..."
                  value={shortInput}
                  disabled={isSubmitted}
                  onChange={e => setShortInput(e.target.value)}
                />
                {isSubmitted && (
                  <div style={styles.correctAnswer}>
                    <span style={{ color: "#4ade80" }}>✓ Expected:</span> {q.answer}
                  </div>
                )}
              </div>
            )}

            {/* Code challenge */}
            {q.type === "code" && (
              <div style={styles.codeArea}>
                <textarea
                  style={styles.codeInput}
                  placeholder="Write your corrected code here..."
                  value={codeInput}
                  disabled={isSubmitted}
                  onChange={e => setCodeInput(e.target.value)}
                  rows={6}
                />
                {isSubmitted && (
                  <div style={styles.codeAnswer}>
                    <div style={{ color: "#4ade80", marginBottom: 6 }}>✓ One correct solution:</div>
                    <pre style={styles.codePre}>{q.answer}</pre>
                  </div>
                )}
              </div>
            )}

            {/* Explanation */}
            {isSubmitted && (
              <div style={styles.explanation}>
                <span style={{ color: color }}>💡 </span>{q.explanation}
              </div>
            )}

            {/* Actions */}
            <div style={styles.actions}>
              {!isSubmitted ? (
                <button style={{ ...styles.submitBtn, background: color, color: "#000" }} onClick={handleSubmit}>
                  Submit Answer
                </button>
              ) : (
                <div style={styles.resultBadge}>
                  {q.type === "multiple"
                    ? multipleCorrect ? "✅ Correct!" : "❌ Incorrect"
                    : "📝 Self-grade this one"}
                </div>
              )}
              <div style={styles.navBtns}>
                <button style={styles.navBtn} onClick={() => goTo(Math.max(0, current - 1))} disabled={current === 0}>← Prev</button>
                <button style={styles.navBtn} onClick={() => goTo(Math.min(total - 1, current + 1))} disabled={current === total - 1}>Next →</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

const styles = {
  root: { minHeight: "100vh", background: "#0d0d1a", color: "#e0e0f0", fontFamily: "'Courier New', monospace", display: "flex", flexDirection: "column" },
  header: { display: "flex", justifyContent: "space-between", alignItems: "center", padding: "16px 24px", borderBottom: "1px solid #1e1e3e", background: "#0a0a14" },
  headerLeft: { display: "flex", alignItems: "center", gap: 12 },
  logo: { fontSize: 22, color: "#00d4ff", fontWeight: "bold" },
  title: { fontSize: 18, fontWeight: "bold", color: "#e0e0f0" },
  progress: { display: "flex", alignItems: "center", gap: 12 },
  progNum: { fontSize: 13, color: "#888" },
  progBar: { width: 120, height: 6, background: "#1a1a2e", borderRadius: 3, overflow: "hidden" },
  progFill: { height: "100%", background: "linear-gradient(90deg, #00d4ff, #a8ff78)", borderRadius: 3, transition: "width 0.3s" },
  body: { display: "flex", flex: 1, overflow: "hidden" },
  sidebar: { width: 220, background: "#0a0a14", borderRight: "1px solid #1e1e3e", padding: 16, overflowY: "auto", display: "flex", flexDirection: "column", gap: 16 },
  sideSection: { display: "flex", flexDirection: "column", gap: 6 },
  sideSectionLabel: { fontSize: 10, fontWeight: "bold", textTransform: "uppercase", letterSpacing: 1 },
  sideNums: { display: "flex", flexWrap: "wrap", gap: 4 },
  sideNum: { width: 28, height: 28, borderRadius: 6, fontSize: 11, fontWeight: "bold", cursor: "pointer", transition: "all 0.15s" },
  finishBtn: { marginTop: "auto", padding: "10px", background: "linear-gradient(135deg, #00d4ff22, #a8ff7822)", border: "1px solid #00d4ff44", borderRadius: 8, color: "#00d4ff", fontSize: 13, cursor: "pointer", fontFamily: "inherit" },
  main: { flex: 1, padding: 24, overflowY: "auto", display: "flex", justifyContent: "center" },
  card: { background: "#13132a", border: "1px solid #2a2a4e", borderRadius: 16, padding: 32, maxWidth: 740, width: "100%", display: "flex", flexDirection: "column", gap: 20 },
  sectionTag: { display: "inline-block", padding: "4px 12px", borderRadius: 20, fontSize: 12, fontWeight: "bold", alignSelf: "flex-start" },
  typeBadge: { fontSize: 11, color: "#666", textTransform: "uppercase", letterSpacing: 1 },
  questionText: { fontSize: 16, lineHeight: 1.7, color: "#dde" },
  codeLine: { display: "block", background: "#0a0a1a", padding: "2px 10px", borderRadius: 4, color: "#a8ff78", fontSize: 14, fontFamily: "monospace", margin: "2px 0" },
  options: { display: "flex", flexDirection: "column", gap: 10 },
  option: { padding: "12px 16px", borderRadius: 10, cursor: "pointer", textAlign: "left", fontSize: 14, display: "flex", alignItems: "center", gap: 12, transition: "all 0.15s", fontFamily: "inherit" },
  optLetter: { width: 24, height: 24, borderRadius: 6, background: "#ffffff11", display: "flex", alignItems: "center", justifyContent: "center", fontSize: 12, fontWeight: "bold", flexShrink: 0 },
  shortArea: { display: "flex", flexDirection: "column", gap: 10 },
  shortInput: { background: "#0a0a1a", border: "2px solid #2a2a4e", borderRadius: 8, padding: "12px 16px", color: "#e0e0f0", fontSize: 14, fontFamily: "monospace", outline: "none" },
  correctAnswer: { padding: "10px 14px", background: "#0a2a0a", border: "1px solid #4ade8044", borderRadius: 8, fontSize: 14, fontFamily: "monospace" },
  codeArea: { display: "flex", flexDirection: "column", gap: 10 },
  codeInput: { background: "#0a0a1a", border: "2px solid #2a2a4e", borderRadius: 8, padding: "12px 16px", color: "#a8ff78", fontSize: 13, fontFamily: "monospace", outline: "none", resize: "vertical", lineHeight: 1.6 },
  codeAnswer: { padding: 14, background: "#0a2a0a", border: "1px solid #4ade8044", borderRadius: 8, fontSize: 13 },
  codePre: { margin: 0, color: "#a8ff78", fontFamily: "monospace", whiteSpace: "pre-wrap" },
  explanation: { padding: "14px 16px", background: "#0f0f2a", border: "1px solid #2a2a5e", borderRadius: 10, fontSize: 14, lineHeight: 1.6, color: "#aab" },
  actions: { display: "flex", alignItems: "center", justifyContent: "space-between", marginTop: 4 },
  submitBtn: { padding: "12px 28px", borderRadius: 10, border: "none", fontSize: 15, fontWeight: "bold", cursor: "pointer", fontFamily: "inherit" },
  resultBadge: { fontSize: 16, fontWeight: "bold" },
  navBtns: { display: "flex", gap: 8 },
  navBtn: { padding: "10px 18px", background: "#1a1a2e", border: "1px solid #2a2a4e", borderRadius: 8, color: "#aaa", cursor: "pointer", fontSize: 13, fontFamily: "inherit" },
  // Score screen
  scoreScreen: { minHeight: "100vh", background: "#0d0d1a", display: "flex", alignItems: "center", justifyContent: "center" },
  scoreCard: { background: "#13132a", border: "1px solid #2a2a4e", borderRadius: 20, padding: 48, textAlign: "center", maxWidth: 480, width: "90%", display: "flex", flexDirection: "column", gap: 16 },
  scoreBig: { fontSize: 80, fontWeight: "bold", background: "linear-gradient(135deg, #00d4ff, #a8ff78)", WebkitBackgroundClip: "text", WebkitTextFillColor: "transparent" },
  scoreLabel: { fontSize: 18, color: "#888" },
  scoreSub: { fontSize: 15, color: "#ccc" },
  scoreBarOuter: { height: 8, background: "#1a1a2e", borderRadius: 4, overflow: "hidden" },
  scoreBarInner: { height: "100%", background: "linear-gradient(90deg, #00d4ff, #a8ff78)", borderRadius: 4, transition: "width 1s" },
  scoreMsg: { fontSize: 18, color: "#e0e0f0", padding: "16px 0" },
  retryBtn: { padding: "14px", background: "linear-gradient(135deg, #00d4ff, #a8ff78)", border: "none", borderRadius: 10, color: "#000", fontWeight: "bold", fontSize: 15, cursor: "pointer", fontFamily: "inherit" },
};
