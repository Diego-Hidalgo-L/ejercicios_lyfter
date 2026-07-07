import { useState } from "react";

const SECTIONS = [
  {
    id: "data_types",
    title: "Data Types & Control Flow",
    icon: "📦",
    color: "#f4a261",
    exercises: [
      {
        id: "dt1",
        title: "Type Arithmetic Predictor",
        difficulty: "Medium",
        description: `Without running the code, predict the result (or error type) for each expression below. Then verify in your Python console.\n\n1. "hello" + " " + "world"\n2. "age: " + 25\n3. [1, 2] + [3, 4]\n4. True + True + False\n5. 3.0 + 2\n6. "ha" * 3\n7. [0] * 4\n8. True * 7\n\nFor each one, write:\n  - Expected result or exception type\n  - Why Python behaves that way`,
        hint: "Remember: Python is strongly typed but dynamic. Some operators are overloaded differently per type.",
        tags: ["types", "operators"]
      },
      {
        id: "dt2",
        title: "Multi-Stage Age Classifier",
        difficulty: "Medium",
        description: `Write a program that:\n1. Asks the user for first name, last name, and age.\n2. Validates that age is a positive integer — if not, keep asking until it is.\n3. Classifies the person into: Baby (0-2), Toddler (3-5), Child (6-12), Pre-teen (11-12), Teenager (13-17), Young adult (18-25), Adult (26-59), Senior (60+).\n4. Greets them by full name and prints their category.\n5. Also prints whether they are legally an adult in most countries (18+) and whether they can run for US President (35+).\n\nExpected output example:\n  Hello, Ada Lovelace!\n  Category: Adult\n  Legal adult: Yes\n  Can run for US President: Yes`,
        hint: "Use elif chains. Remember int() can raise ValueError if input isn't numeric — you'll need a try/except or .isdigit().",
        tags: ["conditionals", "input", "loops"]
      },
      {
        id: "dt3",
        title: "Guess the Number — with lives",
        difficulty: "Medium",
        description: `Build a number guessing game where:\n1. The program picks a SECRET random integer between 1 and 100 (not 1-10).\n2. The player gets exactly 7 attempts.\n3. After each wrong guess, tell the player if the secret is higher or lower AND how many attempts remain.\n4. If the player runs out of attempts, reveal the number.\n5. Track and display the player's best attempt (closest guess).\n\nExample output:\n  Guess a number between 1 and 100: 50\n  Too low! Attempts left: 6\n  Guess a number between 1 and 100: 75\n  Too high! Attempts left: 5\n  ...\n  Game over! The number was 63. Your closest guess was 65.`,
        hint: "Use random.randint(1, 100). Track closest guess by computing abs(guess - secret) each round.",
        tags: ["loops", "random", "conditionals"]
      },
      {
        id: "dt4",
        title: "Grade Statistics Engine",
        difficulty: "Hard",
        description: `Write a program that:\n1. Asks the user how many students there are.\n2. For each student, asks for their name and n grades (you also ask how many grades each student has).\n3. Computes and displays for EACH student:\n   - Their average grade\n   - Their highest and lowest grade\n   - Whether they passed (average >= 70)\n4. Then computes and displays OVERALL statistics:\n   - Class average\n   - Number of students who passed vs failed\n   - The student with the highest average\n   - The student with the lowest average\n\nDo NOT use built-in min(), max(), or sum() — implement those comparisons manually.`,
        hint: "Use nested loops: outer loop for students, inner loop for grades. Store student data in a list of dictionaries.",
        tags: ["loops", "lists", "dicts", "math"]
      }
    ]
  },
  {
    id: "iterations",
    title: "Iterations & Lists",
    icon: "🔁",
    color: "#2ec4b6",
    exercises: [
      {
        id: "it1",
        title: "Parallel List Merger",
        difficulty: "Medium",
        description: `Given two lists of the same size, print their elements side by side — interleaved.\n\nfirst  = ['The', 'quick', 'fox', 'over', 'lazy']\nsecond = ['brown', 'jumps', 'the', 'dog', '!']\n→ "The brown quick jumps fox the over lazy dog !"\n\nRequirements:\n- Use index-based iteration only (no zip, no enumerate tricks — just range)\n- The result must be a single sentence on one line\n- Also print each pair on its own line before the final sentence:\n    Pair 0: The brown\n    Pair 1: quick jumps\n    ...\n    Sentence: The brown quick jumps...`,
        hint: "Use range(len(first_list)) and access both lists with the same index.",
        tags: ["loops", "index", "lists"]
      },
      {
        id: "it2",
        title: "String Reversal & Palindrome Checker",
        difficulty: "Medium",
        description: `Write a program that:\n1. Asks the user to input a sentence.\n2. Prints the sentence reversed character by character.\n3. Also prints each WORD reversed in place (but word order stays the same).\n4. Checks if the original sentence is a palindrome (ignoring spaces and case).\n\nExample:\n  Input:  "racecar is cool"\n  Reversed sentence: "looc si racecar"\n  Words reversed:   "racecar si looc"\n  Is palindrome?    No\n\n  Input:  "never odd or even"\n  Is palindrome? Yes (ignoring spaces)\n\nRestriction: use range() with a step of -1. No slicing allowed.`,
        hint: "To reverse a string, use range(len(s)-1, -1, -1). For words, split on spaces first, reverse each, then rejoin.",
        tags: ["strings", "range", "loops"]
      },
      {
        id: "it3",
        title: "List Transformer",
        difficulty: "Medium",
        description: `Given a list of integers, perform ALL of the following in a single pass (one loop):\n1. Swap the first and last elements.\n2. Remove all odd numbers.\n3. Replace every even number with its square.\n4. Track the running sum as you go.\n\nmy_list = [3, 8, 5, 2, 11, 4, 9, 6]\n\nExpected output:\n  After swap:     [6, 8, 5, 2, 11, 4, 9, 3]\n  Evens squared: [64, 4, 16, 36]\n  Running sums:  [64, 68, 84, 120]\n\nDo NOT use list comprehensions. Build the result lists manually.`,
        hint: "First do the swap (it's just index assignment). Then loop, check even/odd with %, square it, track sum.",
        tags: ["lists", "loops", "math"]
      },
      {
        id: "it4",
        title: "Number Input Tracker",
        difficulty: "Medium",
        description: `Write a program that:\n1. Asks the user to enter exactly 10 numbers, one at a time.\n2. Validates each input — if it's not a valid number, ask again for that slot (don't skip it).\n3. After all 10 are entered, display:\n   - The full list\n   - The maximum (manually, without max())\n   - The minimum (manually, without min())\n   - The average\n   - How many are above the average\n   - The index of the maximum value\n\nNo built-in max(), min(), or sum() allowed.`,
        hint: "Use a while loop with a counter. Increment counter only on valid input. Track max/min by comparison as you go.",
        tags: ["input", "validation", "lists", "loops"]
      },
      {
        id: "it5",
        title: "Above-Average Filter + Word Length Gate",
        difficulty: "Hard",
        description: `Part A — Numbers:\nGiven a list of numbers, compute the average (no sum() or statistics module), then build a NEW list with only numbers above average. Print both.\n\nmy_list = [10, 20, 30, 40, 50, 15, 25]\n→ Average: 27.14\n→ Above average: [30, 40, 50]\n\nPart B — Words:\nAsk the user to input 6 words separated by spaces. Then:\n- Filter only words longer than 4 characters\n- Sort them alphabetically (implement bubble sort for strings — yes, really)\n- Display the sorted filtered list\n\nExample:\n  Input: "cat elephant sun programming loop sky"\n  Filtered (>4 chars): ['elephant', 'programming']\n  Sorted: ['elephant', 'programming']`,
        hint: "For Part B, use your bubble sort from scratch. Strings are compared with > and < in Python lexicographically.",
        tags: ["lists", "sorting", "bubble sort", "strings"]
      },
      {
        id: "it6",
        title: "Sales Total by UPC",
        difficulty: "Hard",
        description: `Given this sales data, compute total revenue per UPC WITHOUT using dict methods like .get() inside the accumulation — use if/else to check key existence.\n\nsales = [\n  {'date':'2024-01-01','email':'a@x.com','items':[\n    {'name':'Lamp','upc':'ITEM-1','unit_price':30.00},\n    {'name':'Fan','upc':'ITEM-2','unit_price':45.50},\n  ]},\n  {'date':'2024-01-02','email':'b@x.com','items':[\n    {'name':'Lamp','upc':'ITEM-1','unit_price':30.00},\n    {'name':'Mat','upc':'ITEM-3','unit_price':12.00},\n  ]},\n  {'date':'2024-01-02','email':'c@x.com','items':[\n    {'name':'Fan','upc':'ITEM-2','unit_price':45.50},\n    {'name':'Fan','upc':'ITEM-2','unit_price':45.50},\n  ]},\n]\n\nExpected output:\n  ITEM-1: $60.00\n  ITEM-2: $136.50\n  ITEM-3: $12.00\n\nBonus: also print which UPC had the highest total revenue.`,
        hint: "Outer loop over sales, inner loop over items. Check if upc key exists in result dict, add or initialize.",
        tags: ["dicts", "nested loops", "lists"]
      }
    ]
  },
  {
    id: "exceptions",
    title: "Exceptions & Error Handling",
    icon: "🚨",
    color: "#e63946",
    exercises: [
      {
        id: "ex1",
        title: "Bulletproof Command-Line Calculator",
        difficulty: "Hard",
        description: `Build a command-line calculator that:\n1. Starts with a current result of 0.\n2. Displays a menu: (1) Add  (2) Subtract  (3) Multiply  (4) Divide  (5) Clear  (6) Quit\n3. After choosing an operation, asks for a number.\n4. Handles ALL of these errors gracefully (no crashes):\n   - Invalid menu option (not 1-6)\n   - Non-numeric input for the number\n   - Division by zero\n   - Overflow (if result exceeds 1,000,000, warn the user but keep going)\n5. Shows the current result after every operation.\n6. Keeps a history list of all operations performed and displays it when quitting.\n\nExample:\n  Current: 0\n  Choose operation: 1\n  Enter number: 10\n  Current: 10\n  Choose operation: 4\n  Enter number: 0\n  Error: Cannot divide by zero!\n  Current: 10 (unchanged)`,
        hint: "Wrap each operation in its own try/except. Use a list to store history strings like '10 + 5 = 15'.",
        tags: ["exceptions", "loops", "dicts", "validation"]
      },
      {
        id: "ex2",
        title: "List Converter with Full Error Report",
        difficulty: "Medium",
        description: `Write a function convert_list(items) that:\n1. Receives a list of mixed values.\n2. Tries to convert each to float.\n3. Collects ALL successes AND failures (don't stop on first error).\n4. At the end prints:\n   - Successfully converted values\n   - Items that failed and why\n   - The sum of successful conversions\n   - The percentage of items that converted successfully\n\nmy_list = ['3.5', 'hello', '10', None, '7', 'NaN', '4.2']\n\nExpected output:\n  ✓ '3.5' → 3.5\n  ✗ 'hello' → ValueError: could not convert\n  ✓ '10' → 10.0\n  ✗ None → TypeError: float() argument must be string or number\n  ✓ '7' → 7.0\n  ✗ 'NaN' → converted but invalid — handle this separately!\n  ✓ '4.2' → 4.2\n  Sum: 24.7  |  Success rate: 57.1%`,
        hint: "Catch both ValueError AND TypeError. For NaN, check math.isnan() after conversion. Keep two lists: good and bad.",
        tags: ["exceptions", "functions", "lists", "types"]
      },
      {
        id: "ex3",
        title: "User Registration with Chained Validation",
        difficulty: "Hard",
        description: `Write a program that registers a user by asking for:\n1. Username — must be 3-20 chars, only letters/numbers/underscores, not purely numeric\n2. Email — must contain exactly one '@' and at least one '.' after the '@'\n3. Age — must be an integer between 13 and 120\n4. Password — must be at least 8 characters, contain at least one digit\n\nFor each field:\n- If invalid, raise a ValueError with a descriptive message and ask again\n- Catch it, print the error, and retry that field (not the whole form)\n- After 3 failed attempts on any field, raise a RuntimeError('Too many failed attempts') and exit\n\nOn success, print: "Registration complete: {username}, {email}, age {age}"`,
        hint: "Use a helper function like validate_field(prompt, validator_fn, max_attempts=3) that loops and counts failures.",
        tags: ["exceptions", "validation", "raise", "loops"]
      }
    ]
  },
  {
    id: "scope",
    title: "Scope & Functions",
    icon: "🔭",
    color: "#9b5de5",
    exercises: [
      {
        id: "sc1",
        title: "Prime Number Filter",
        difficulty: "Hard",
        description: `Write two functions:\n1. is_prime(n) → returns True if n is prime, False otherwise.\n   - Must handle edge cases: negatives, 0, 1 (none are prime)\n   - Must work for large numbers (optimize: only check up to √n)\n2. get_primes(numbers_list) → returns a new list with only the prime numbers.\n\nTest it with:\n  [1, 2, 3, 4, 13, 15, 17, 19, 20, 97, 100, 101]\n  → [2, 3, 13, 17, 19, 97, 101]\n\nBonus: also write a function prime_gaps(numbers_list) that returns a list of the differences between consecutive primes in the result.\n  [2, 3, 13, 17, 19, 97, 101]\n  gaps → [1, 10, 4, 2, 78, 4]`,
        hint: "For √n, use n**0.5 or import math and use math.sqrt(). Check divisibility from 2 to int(n**0.5)+1.",
        tags: ["functions", "math", "lists", "scope"]
      },
      {
        id: "sc2",
        title: "String Toolkit",
        difficulty: "Medium",
        description: `Build a module of 4 string utility functions. Each must be its own function and they may call each other:\n\n1. count_char_occurrences(text, char) → int\n   "programming", "g" → 2\n\n2. count_vowels(text) → int\n   "Hello World" → 3\n\n3. reverse_words_alphabetically(sentence) → str\n   Input is a hyphen-separated string\n   "python-variable-function-computer" → "computer-function-python-variable"\n\n4. word_frequency(text) → dict\n   "the cat sat on the mat the cat" → {'the':3,'cat':2,'sat':1,'on':1,'mat':1}\n   (do NOT use collections.Counter)\n\nFor each function, also print a one-line description of what it does before calling it.`,
        hint: "For word_frequency, loop through words and use if/else to check if the key already exists in the dict.",
        tags: ["functions", "strings", "dicts"]
      },
      {
        id: "sc3",
        title: "Scope Bug Hunt",
        difficulty: "Medium",
        description: `The following code has 4 scope-related bugs. Find and fix ALL of them. For each bug, write a comment explaining what was wrong.\n\n--- BUGGY CODE ---\ncounter = 0\n\ndef increment():\n    counter += 1\n\ndef get_double(n):\n    result = n * 2\n\ndef process_list(items):\n    total = 0\n    for item in items:\n        sub_total = sub_total + item\n    total += sub_total\n    return total\n\ndef make_multiplier(factor):\n    def multiply(x):\n        return x * Factor  # intentional bug\n    return multiply\n\nincrement()\nprint(counter)\nprint(get_double(5))\nprint(process_list([1, 2, 3]))\ndouble = make_multiplier(2)\nprint(double(10))\n---\n\nWrite the corrected code with explanatory comments.`,
        hint: "Issues: global variable mutation, missing return, variable used before assignment, wrong capitalization of closure variable.",
        tags: ["scope", "bugs", "closures", "global"]
      },
      {
        id: "sc4",
        title: "Case Counter & Alphabetical Sorter",
        difficulty: "Medium",
        description: `Write two functions:\n\n1. count_cases(text) → prints and returns a tuple (upper_count, lower_count)\n   - Count only actual letters (ignore spaces, digits, punctuation)\n   "I Love Nación Sushi!" → upper: 3, lower: 13\n\n2. sort_hyphenated(text) → str\n   - Takes a hyphen-separated string of words\n   - Returns them sorted alphabetically WITHOUT using sorted() or .sort()\n   - Implement your own sort (bubble sort is fine)\n   "python-variable-function-computer-monitor"\n   → "computer-function-monitor-python-variable"\n\nThen write a main() function that:\n- Asks for a sentence and calls count_cases()\n- Asks for a hyphenated string and calls sort_hyphenated()\n- Prints the results clearly`,
        hint: "Use .isupper() and .islower() and .isalpha() for case counting. For sort, split('-'), bubble sort, then '-'.join().",
        tags: ["strings", "functions", "sorting"]
      }
    ]
  },
  {
    id: "file_handling",
    title: "File Handling",
    icon: "📁",
    color: "#06d6a0",
    exercises: [
      {
        id: "fh1",
        title: "Song Sorter",
        difficulty: "Medium",
        description: `Write a program that:\n1. Creates a file called songs_input.txt with at least 8 song titles (write them in code, one per line — hardcode them).\n2. Reads the file back.\n3. Strips all whitespace/newlines from each line.\n4. Sorts them alphabetically WITHOUT using sorted() — implement bubble sort.\n5. Writes the sorted list to songs_sorted.txt, one per line.\n6. Reads and prints the final sorted file to confirm.\n\nBonus: also write a third file songs_reversed.txt with the sorted list in reverse order.\n\nAll file operations must use the with open(...) as f: pattern.`,
        hint: "Read with readlines(), strip each line, bubble sort the list, write with a loop using f.write(song + '\\n').",
        tags: ["files", "sorting", "strings"]
      },
      {
        id: "fh2",
        title: "Text File Analyzer",
        difficulty: "Hard",
        description: `Write a program that:\n1. Creates a text file with at least 5 lines of varied content (hardcode it).\n2. Opens and analyzes the file to produce a report saved in report.txt:\n   - Total number of lines\n   - Total number of words\n   - Total number of characters (with and without spaces)\n   - The longest word found\n   - The most common word (implement frequency count manually — no Counter)\n   - Lines converted to UPPERCASE\n3. Prints the report to console AND writes it to report.txt.\n\nAll file ops must use with open(). Use encoding='utf-8' everywhere.`,
        hint: "Read with readlines(). For each line, split() to get words. Track longest word by comparing len() manually.",
        tags: ["files", "strings", "dicts", "analysis"]
      },
      {
        id: "fh3",
        title: "Videogame CSV Manager",
        difficulty: "Hard",
        description: `Build a full CSV management program for videogames:\n\nFields: name, genre, developer, esrb_rating, release_year, metacritic_score\n\nFeatures:\n1. Add a new game (validate: year must be 1970-2025, score 0-100, rating one of E/T/M/AO)\n2. Read and display ALL games in a formatted table\n3. Filter games by ESRB rating\n4. Filter games by developer (case-insensitive)\n5. Count games per genre and display sorted by count (most to least)\n6. Find the highest-rated game per genre\n\nAll operations persist to games.csv. Use csv.DictReader and csv.DictWriter.\nHandle the case where the file doesn't exist yet (first run).`,
        hint: "Wrap file reads in try/except FileNotFoundError. For sorting genre counts, build a list of (genre, count) tuples and bubble sort by count.",
        tags: ["files", "csv", "dicts", "validation"]
      },
      {
        id: "fh4",
        title: "Pokémon JSON Database",
        difficulty: "Hard",
        description: `Build a Pokémon manager that reads/writes a JSON file.\n\nEach Pokémon has: name, types (list), base_stats (dict with hp, attack, defense, speed)\n\nFeatures:\n1. Add a new Pokémon (validate all fields — types must be a non-empty list, all stats must be positive integers)\n2. List all Pokémon with their stats\n3. Filter by type (e.g., show all "Fire" types)\n4. Show the Pokémon with the highest total base stats (sum of all stats)\n5. Group Pokémon by type and show average stats per type\n6. Remove a Pokémon by name\n\nSeed the file with at least 5 Pokémon if it doesn't exist. Use json.load() and json.dump() with indent=2.`,
        hint: "For grouping by type, a Pokémon can have multiple types — each type entry gets the Pokémon. Build a dict of type → list of Pokémon.",
        tags: ["files", "json", "dicts", "lists"]
      }
    ]
  },
  {
    id: "inf_params",
    title: "Infinite Parameters",
    icon: "♾️",
    color: "#f72585",
    exercises: [
      {
        id: "ip1",
        title: "Flexible Statistics Calculator",
        difficulty: "Medium",
        description: `Write a function stats(*numbers, **options) that:\n- Accepts any number of numeric arguments\n- Accepts keyword arguments to control output:\n  - include_sum=True/False\n  - include_average=True/False  \n  - include_min=True/False\n  - include_max=True/False\n  - round_to=2 (number of decimal places)\n- Computes only the requested statistics\n- Returns a dict with the requested results\n\nDo NOT use built-in sum(), min(), max() — implement manually.\n\nExample:\n  stats(4, 7, 2, 9, 1, include_sum=True, include_average=True, round_to=1)\n  → {'sum': 23, 'average': 4.6}\n\n  stats(10, 5, 8, include_min=True, include_max=True)\n  → {'min': 5, 'max': 10}`,
        hint: "Use *numbers to capture positional args. Use **options.get('include_sum', False) to check each option. Build result dict conditionally.",
        tags: ["*args", "**kwargs", "functions"]
      },
      {
        id: "ip2",
        title: "Log Decorator Factory",
        difficulty: "Hard",
        description: `Write a function make_logger(prefix, **log_options) that RETURNS a decorator.\nThe decorator wraps any function and:\n- Prints: "{prefix} | Calling: {func_name} | Args: {args} | Kwargs: {kwargs}"\n- Calls the original function\n- If log_options['log_result'] is True, prints: "{prefix} | Result: {result}"\n- If log_options['log_time'] is True, prints how long the function took (use time.time())\n\nThe wrapped function must accept *args and **kwargs.\n\nExample:\n  @make_logger("APP", log_result=True, log_time=True)\n  def multiply(*nums):\n      result = 1\n      for n in nums: result *= n\n      return result\n\n  multiply(3, 4, 5)\n  → APP | Calling: multiply | Args: (3, 4, 5) | Kwargs: {}\n  → APP | Result: 60\n  → APP | Time: 0.0001s`,
        hint: "make_logger returns a decorator, which returns a wrapper. Three levels of nesting. The inner wrapper uses *args, **kwargs to pass everything through.",
        tags: ["*args", "**kwargs", "decorators", "closures"]
      },
      {
        id: "ip3",
        title: "Table Printer",
        difficulty: "Medium",
        description: `Write a function print_table(*rows, **formatting) that:\n- Each row is a tuple or list of values\n- Keyword args control formatting:\n  - separator='|' (column separator)\n  - padding=2 (spaces around each value)\n  - header=True (if True, print a divider line after the first row)\n  - align='left' or 'right'\n\nExample:\n  print_table(\n    ('Name', 'Age', 'City'),\n    ('Alice', 30, 'NYC'),\n    ('Bob', 25, 'LA'),\n    separator='|', padding=1, header=True, align='left'\n  )\n\nOutput:\n  | Name  | Age | City |\n  |-------|-----|------|\n  | Alice | 30  | NYC  |\n  | Bob   | 25  | LA   |`,
        hint: "First pass: compute max column widths by iterating all rows. Second pass: format and print each row using those widths.",
        tags: ["*args", "**kwargs", "strings", "formatting"]
      }
    ]
  },
  {
    id: "decorators",
    title: "Decorators",
    icon: "🎀",
    color: "#ff6b6b",
    exercises: [
      {
        id: "dc1",
        title: "Signature Logger Decorator",
        difficulty: "Medium",
        description: `Write a decorator @log_signature that:\n1. Prints the function name before calling it\n2. Prints each parameter name and its value\n3. Calls the function\n4. Prints the return value\n5. Prints a separator line after\n\nThen apply it to 3 different functions:\n- add(a, b)\n- greet(name, greeting="Hello")\n- power(base, exponent, mod=None)\n\nExample output for add(3, 5):\n  ┌─ Calling: add\n  │  a = 3\n  │  b = 5\n  │  → Result: 8\n  └──────────────`,
        hint: "Use functools.wraps to preserve the original function's metadata. Access parameter names with inspect.signature() or just use *args/**kwargs.",
        tags: ["decorators", "functions", "logging"]
      },
      {
        id: "dc2",
        title: "Type Guard Decorator",
        difficulty: "Hard",
        description: `Write a decorator @validate_numbers that:\n- Checks that ALL positional arguments are numeric (int or float)\n- If any argument is not numeric, raises TypeError with a message like:\n  "Argument 2 ('hello') is not a number"\n- Does NOT affect keyword arguments\n\nThen write a second decorator @clamp(min_val, max_val) that:\n- Wraps the function's RETURN VALUE\n- If the result is below min_val, returns min_val instead\n- If above max_val, returns max_val\n- Prints a warning if clamping occurred\n\nApply both to a function calculate(*nums) that returns their product:\n  @clamp(0, 1000)\n  @validate_numbers\n  def calculate(*nums):\n      result = 1\n      for n in nums: result *= n\n      return result\n\n  calculate(3, 4, 5)     → 60\n  calculate(5, 5, 5, 5)  → 1000 (clamped!) with warning\n  calculate(2, 'x', 4)  → TypeError`,
        hint: "@clamp is a decorator factory — it takes arguments and returns a decorator. Stack them: @clamp applied last is outermost wrapper.",
        tags: ["decorators", "factories", "*args", "validation"]
      },
      {
        id: "dc3",
        title: "Adult-Only Access Decorator",
        difficulty: "Hard",
        description: `Build a system with:\n\n1. A User class with attributes: name, date_of_birth (a date object), role ('admin' or 'user')\n   - A @property age that computes age from date_of_birth\n\n2. A decorator @requires_adult that:\n   - Checks if the FIRST argument (a User instance) is 18+\n   - If not, raises PermissionError("User {name} is underage")\n\n3. A decorator @requires_role(role) that:\n   - Checks if the User's role matches the required role\n   - If not, raises PermissionError("Role '{role}' required")\n\n4. Apply both to functions:\n   @requires_role('admin')\n   @requires_adult\n   def delete_records(user): ...\n\n   @requires_adult\n   def view_content(user): ...\n\nTest with users of different ages and roles.`,
        hint: "@requires_role is a decorator factory. @requires_adult is a regular decorator. Stack them: the outermost decorator runs its check first.",
        tags: ["decorators", "OOP", "properties", "validation"]
      }
    ]
  },
  {
    id: "oop",
    title: "Object-Oriented Programming",
    icon: "🏗️",
    color: "#4cc9f0",
    exercises: [
      {
        id: "oop1",
        title: "Shape Hierarchy",
        difficulty: "Hard",
        description: `Build a shape class hierarchy:\n\n1. Abstract base class Shape:\n   - Abstract methods: calculate_area(), calculate_perimeter()\n   - Concrete method: describe() → prints name, area, and perimeter\n   - Abstract property: name\n\n2. Implement: Circle(radius), Rectangle(width, height), Triangle(a, b, c)\n   - Triangle: validate that the three sides form a valid triangle (triangle inequality)\n   - All: validate that dimensions are positive, raise ValueError if not\n\n3. Add a @classmethod from_string(cls, s) to each that parses:\n   - Circle: "circle:5" → Circle(5)\n   - Rectangle: "rect:4x6" → Rectangle(4, 6)\n   - Triangle: "tri:3,4,5" → Triangle(3,4,5)\n\n4. Write a function total_area(*shapes) that returns the combined area of any number of shapes.\n\nTest with a mixed list of shapes and call describe() on each.`,
        hint: "For Triangle area, use Heron's formula: s=(a+b+c)/2, area=√(s(s-a)(s-b)(s-c)). Import math for sqrt and pi.",
        tags: ["OOP", "abstract", "inheritance", "properties"]
      },
      {
        id: "oop2",
        title: "Bank Account System",
        difficulty: "Hard",
        description: `Build a banking system:\n\n1. BankAccount:\n   - Private __balance, __owner, __transaction_history (list)\n   - deposit(amount): validates > 0, adds to balance, logs to history\n   - withdraw(amount): validates > 0 and sufficient funds, deducts, logs\n   - @property balance: returns balance (read-only)\n   - print_statement(): prints all transactions with running balance\n   - transfer(amount, other_account): withdraws from self, deposits to other\n\n2. SavingsAccount(BankAccount):\n   - Additional __min_balance attribute\n   - Overrides withdraw() to prevent balance going below min_balance\n   - @property interest_rate (default 0.05)\n   - apply_interest(): adds interest to balance\n\n3. PremiumAccount(SavingsAccount):\n   - Overrides interest_rate to 0.08\n   - add bonus: every 5th deposit triggers a $10 bonus automatically\n\nTest: create accounts, transfer between them, apply interest, print statements.`,
        hint: "Use super().withdraw() in SavingsAccount but add your balance check before calling it. Track deposit count for PremiumAccount bonus.",
        tags: ["OOP", "inheritance", "encapsulation", "properties"]
      },
      {
        id: "oop3",
        title: "Human Body Model",
        difficulty: "Medium",
        description: `Create a class for each body part with meaningful attributes and methods:\n\nHand: fingers (5), can grip(object_name) → prints action\nArm: has a Hand, can reach(distance) → prints if reachable (max 1.5m)\nLeg: has a Foot, can kick(force) → prints action\nFoot: toes (5), shoe_size\nTorso: has Head, two Arms, two Legs\nHead: has Brain and two Eyes; Eyes have color; Brain has iq\nHuman: has a Torso, name, age\n  - walk(steps): uses both legs\n  - wave(): uses right arm's hand\n  - think(thought): uses brain (print thought)\n  - __str__(): returns summary like "Alice, age 30, IQ: 120"\n\nInstantiate a full Human and demonstrate all actions.`,
        hint: "Start from the smallest classes (Hand, Foot, Eye, Brain) and build up. Pass instances as constructor arguments.",
        tags: ["OOP", "composition", "classes"]
      },
      {
        id: "oop4",
        title: "Smart Bus System",
        difficulty: "Hard",
        description: `Build a bus/passenger system:\n\n1. Person class (from lesson): name, age\n   - @property is_adult → age >= 18\n\n2. Bus class:\n   - Attributes: route_number, max_passengers, current_stop\n   - Private __passengers list (starts empty)\n   - board(person): add if space and person is adult; else specific error message\n   - board_group(*people): boards multiple people, reports who boarded and who didn't\n   - exit(person_name): removes passenger by name, raises ValueError if not found\n   - next_stop(stop_name): updates current stop, prints announcement\n   - @property passenger_count\n   - @property is_full\n   - manifest(): prints all current passengers and current stop\n\n3. BusFleet class:\n   - Manages multiple buses\n   - add_bus(bus)\n   - find_bus_with_space(): returns first bus with available space\n   - total_passengers(): sum across all buses\n   - fleet_report(): prints info for all buses`,
        hint: "Use a list comprehension (or manual loop) for board_group. For exit(), iterate with enumerate to find index, then pop.",
        tags: ["OOP", "classes", "lists", "encapsulation"]
      }
    ]
  },
  {
    id: "data_structures",
    title: "Data Structures",
    icon: "🔗",
    color: "#b5ead7",
    exercises: [
      {
        id: "ds1",
        title: "Full Linked List",
        difficulty: "Hard",
        description: `Build a LinkedList class with Node support:\n\nMethods:\n- insert_front(data): inserts at head\n- insert_back(data): inserts at tail\n- insert_at(index, data): inserts at given index (raise IndexError if out of range)\n- delete(data): removes first node with given value\n- delete_at(index): removes node at given index\n- find(data) → int: returns index of first occurrence, -1 if not found\n- reverse(): reverses the list IN PLACE (no new list)\n- print_all(): prints as "A -> B -> C -> None"\n- __len__(): returns number of nodes\n\nTest sequence:\n  insert_back(1,2,3,4,5)\n  insert_front(0)\n  insert_at(3, 99)\n  print → 0 -> 1 -> 2 -> 99 -> 3 -> 4 -> 5 -> None\n  delete(99)\n  reverse()\n  print → 5 -> 4 -> 3 -> 2 -> 1 -> 0 -> None`,
        hint: "For reverse(): use three pointers — prev, current, next_node. Walk the list updating each node's .next to point backward.",
        tags: ["linked list", "OOP", "data structures"]
      },
      {
        id: "ds2",
        title: "Stack with Undo History",
        difficulty: "Hard",
        description: `Build a Stack using only Node objects (no lists/dicts/tuples).\n\nMethods:\n- push(data): adds to top\n- pop(): removes and returns top element; raises IndexError if empty\n- peek(): returns top without removing; raises IndexError if empty\n- is_empty() → bool\n- size() → int (walk the nodes to count)\n- print_all(): prints top to bottom\n\nThen use your Stack to implement a simple text editor buffer:\n- type(text): pushes text to the stack (represents typing an action)\n- undo(): pops the last action\n- redo(): (needs a second stack!) re-applies an undone action\n- current_state(): shows what's currently in the main stack\n\nDemo with a sequence of type/undo/redo operations.`,
        hint: "Redo stack: when you undo, push the action to redo_stack. When you type something NEW, clear redo_stack. This is exactly how most editors work.",
        tags: ["stack", "linked list", "OOP", "data structures"]
      },
      {
        id: "ds3",
        title: "Double Ended Queue",
        difficulty: "Hard",
        description: `Build a Deque (Double Ended Queue) using only Node objects.\n\nEach node needs: data, next, prev (doubly linked).\n\nMethods:\n- push_left(data): insert at front\n- push_right(data): insert at back\n- pop_left(): remove and return from front\n- pop_right(): remove and return from back\n- peek_left() / peek_right(): look without removing\n- is_empty() → bool\n- size() → int\n- print_forward(): head → tail\n- print_backward(): tail → head\n\nThen demonstrate by implementing a "sliding window max" algorithm:\nGiven a list of numbers and window size k, use your Deque to find the maximum in each window of size k.\n  [3, 1, 3, 2, 5, 4], k=3 → [3, 3, 5, 5]`,
        hint: "Doubly linked nodes make pop_right O(1) since you have the tail pointer. For sliding window, the Deque stores indices into the original list.",
        tags: ["deque", "doubly linked", "OOP", "algorithms"]
      },
      {
        id: "ds4",
        title: "Binary Tree Traversals",
        difficulty: "Hard",
        description: `Build a Binary Tree where each node has data, left, right.\n\nMethods on BinaryTree:\n- insert(data): insert maintaining BST property (left < root < right)\n- search(data) → bool: returns True if found\n- Three traversal methods (all print the values):\n  - inorder(): left → root → right (gives sorted order for BST)\n  - preorder(): root → left → right\n  - postorder(): left → right → root\n- height() → int: returns tree height\n- count_leaves() → int: nodes with no children\n- print_level_by_level(): use a Queue to print level by level\n  (you can use your Queue implementation from before!)\n\nInsert: 5, 3, 7, 1, 4, 6, 8\nExpect inorder: 1, 3, 4, 5, 6, 7, 8`,
        hint: "All traversals are naturally recursive. For height: max(height(left), height(right)) + 1. Base case: None node has height -1 or 0.",
        tags: ["binary tree", "recursion", "OOP", "data structures"]
      }
    ]
  },
  {
    id: "algorithms",
    title: "Algorithms & Big O",
    icon: "📈",
    color: "#ffd166",
    exercises: [
      {
        id: "al1",
        title: "Bubble Sort Variants",
        difficulty: "Hard",
        description: `Implement THREE versions of Bubble Sort:\n\n1. Standard bubble_sort(lst): sorts ascending, returns sorted list.\n   - Include the has_made_changes optimization.\n   - Include the outer_index optimization.\n\n2. bubble_sort_desc(lst): sorts DESCENDING (right to left — small numbers bubble left).\n\n3. bubble_sort_linked(linked_list): sorts a LinkedList IN PLACE by swapping DATA (not nodes).\n   - You can reuse your LinkedList from the data structures section.\n\n4. bubble_sort_steps(lst): returns a dict:\n   {'sorted': [...], 'passes': n, 'swaps': n, 'comparisons': n}\n\nTest all 4 with: [64, 34, 25, 12, 22, 11, 90]`,
        hint: "For descending, just flip the comparison: if current < next: swap. For linked list, walk nodes swapping .data not the nodes themselves.",
        tags: ["bubble sort", "linked list", "algorithms"]
      },
      {
        id: "al2",
        title: "Big O Analysis Lab",
        difficulty: "Hard",
        description: `Analyze the Big O complexity of each algorithm below. For each one:\n1. State the time complexity\n2. Explain WHY (which part dominates)\n3. State the space complexity\n4. Describe the best case vs worst case\n\n--- ALGORITHM A ---\ndef find_duplicates(lst):\n    duplicates = []\n    for i in range(len(lst)):\n        for j in range(i+1, len(lst)):\n            if lst[i] == lst[j] and lst[i] not in duplicates:\n                duplicates.append(lst[i])\n    return duplicates\n\n--- ALGORITHM B ---\ndef binary_search(lst, target):\n    low, high = 0, len(lst) - 1\n    while low <= high:\n        mid = (low + high) // 2\n        if lst[mid] == target: return mid\n        elif lst[mid] < target: low = mid + 1\n        else: high = mid - 1\n    return -1\n\n--- ALGORITHM C ---\ndef flatten(nested):\n    result = []\n    for item in nested:\n        if isinstance(item, list):\n            for sub in item:\n                result.append(sub)\n        else:\n            result.append(item)\n    return result\n\n--- ALGORITHM D ---\ndef power_set(lst):\n    result = [[]]\n    for item in lst:\n        result += [subset + [item] for subset in result]\n    return result\n\nBonus: propose a more efficient version of Algorithm A.`,
        hint: "For D: each element doubles the result set size → 2^n subsets → O(2^n). The nested loop in A checks (n*(n-1))/2 pairs → O(n²).",
        tags: ["Big O", "analysis", "algorithms"]
      },
      {
        id: "al3",
        title: "Algorithm Comparison Benchmark",
        difficulty: "Hard",
        description: `Implement and empirically compare two search algorithms:\n\n1. linear_search(lst, target) → index or -1\n   Big O: ?\n\n2. binary_search(lst, target) → index or -1\n   (list must be sorted; if not sorted, sort it first)\n   Big O: ?\n\nBenchmark both:\n- Generate sorted lists of sizes: 100, 1000, 10000, 100000\n- For each size, time BOTH searches looking for:\n  a) An element at the beginning\n  b) An element in the middle\n  c) An element at the end\n  d) An element that doesn't exist\n- Use time.time() before and after each call\n- Print a comparison table\n\nAnalysis questions (write as comments):\n- At what size does binary_search become significantly faster?\n- What is the requirement for binary_search that linear_search doesn't have?\n- When would you choose linear over binary despite it being slower?`,
        hint: "Use random module to generate lists. Sort with sorted() for the binary search tests. Format time output in microseconds (multiply by 1_000_000).",
        tags: ["Big O", "algorithms", "benchmarking", "search"]
      }
    ]
  }
];

const DIFFICULTY_COLORS = {
  Easy: "#4ade80",
  Medium: "#fbbf24",
  Hard: "#f87171"
};

export default function CodingPractice() {
  const [activeSection, setActiveSection] = useState(0);
  const [completedExercises, setCompletedExercises] = useState({});
  const [expandedExercise, setExpandedExercise] = useState(null);
  const [showHint, setShowHint] = useState({});
  const [notes, setNotes] = useState({});

  const section = SECTIONS[activeSection];
  const totalExercises = SECTIONS.reduce((a, s) => a + s.exercises.length, 0);
  const completedCount = Object.values(completedExercises).filter(Boolean).length;

  function toggleComplete(id) {
    setCompletedExercises(p => ({ ...p, [id]: !p[id] }));
  }

  function toggleHint(id) {
    setShowHint(p => ({ ...p, [id]: !p[id] }));
  }

  function toggleExpand(id) {
    setExpandedExercise(expandedExercise === id ? null : id);
    setShowHint(p => ({ ...p, [id]: false }));
  }

  const pct = Math.round((completedCount / totalExercises) * 100);
  const sectionCompleted = section.exercises.filter(e => completedExercises[e.id]).length;

  return (
    <div style={S.root}>
      {/* Sidebar */}
      <div style={S.sidebar}>
        <div style={S.sideHeader}>
          <div style={S.sideTitle}>Practice</div>
          <div style={S.sideSubtitle}>Coding Exercises</div>
          <div style={S.globalProgress}>
            <div style={S.gpLabel}>{completedCount}/{totalExercises} done</div>
            <div style={S.gpBar}><div style={{...S.gpFill, width:`${pct}%`}}/></div>
          </div>
        </div>
        <div style={S.navList}>
          {SECTIONS.map((s, i) => {
            const done = s.exercises.filter(e => completedExercises[e.id]).length;
            return (
              <button key={s.id} onClick={() => { setActiveSection(i); setExpandedExercise(null); }}
                style={{
                  ...S.navItem,
                  background: activeSection === i ? s.color + "22" : "transparent",
                  borderLeft: activeSection === i ? `3px solid ${s.color}` : "3px solid transparent",
                  color: activeSection === i ? s.color : "#888"
                }}>
                <span style={S.navIcon}>{s.icon}</span>
                <div style={S.navText}>
                  <div style={S.navName}>{s.title}</div>
                  <div style={S.navCount}>{done}/{s.exercises.length}</div>
                </div>
                {done === s.exercises.length && <span style={S.checkAll}>✓</span>}
              </button>
            );
          })}
        </div>
      </div>

      {/* Main */}
      <div style={S.main}>
        {/* Section Header */}
        <div style={{...S.sectionHeader, borderBottom: `2px solid ${section.color}44`}}>
          <div style={{...S.sectionIcon, color: section.color}}>{section.icon}</div>
          <div>
            <div style={{...S.sectionTitle, color: section.color}}>{section.title}</div>
            <div style={S.sectionMeta}>{sectionCompleted}/{section.exercises.length} exercises completed</div>
          </div>
          <div style={{...S.sectionPct, color: section.color}}>
            {Math.round((sectionCompleted/section.exercises.length)*100)}%
          </div>
        </div>

        {/* Exercises */}
        <div style={S.exerciseList}>
          {section.exercises.map((ex, idx) => {
            const isExpanded = expandedExercise === ex.id;
            const isDone = completedExercises[ex.id];
            const hintVisible = showHint[ex.id];
            return (
              <div key={ex.id} style={{
                ...S.exerciseCard,
                border: `1px solid ${isDone ? section.color + "88" : "#2a2a4e"}`,
                background: isDone ? section.color + "08" : "#13132a"
              }}>
                {/* Card Header */}
                <div style={S.cardHeader} onClick={() => toggleExpand(ex.id)}>
                  <div style={S.cardLeft}>
                    <div style={{...S.exNum, color: section.color}}>#{idx+1}</div>
                    <div>
                      <div style={S.exTitle}>{ex.title}</div>
                      <div style={S.tagRow}>
                        <span style={{...S.diffBadge, background: DIFFICULTY_COLORS[ex.difficulty] + "22", color: DIFFICULTY_COLORS[ex.difficulty]}}>
                          {ex.difficulty}
                        </span>
                        {ex.tags.slice(0,3).map(t => (
                          <span key={t} style={S.tag}>{t}</span>
                        ))}
                      </div>
                    </div>
                  </div>
                  <div style={S.cardRight}>
                    <button onClick={e => { e.stopPropagation(); toggleComplete(ex.id); }}
                      style={{...S.doneBtn, background: isDone ? section.color : "transparent", borderColor: isDone ? section.color : "#444", color: isDone ? "#000" : "#666"}}>
                      {isDone ? "✓ Done" : "Mark Done"}
                    </button>
                    <span style={{color: "#555", fontSize: 18}}>{isExpanded ? "▲" : "▼"}</span>
                  </div>
                </div>

                {/* Expanded Content */}
                {isExpanded && (
                  <div style={S.cardBody}>
                    <div style={S.descBlock}>
                      {ex.description.split("\n").map((line, i) => {
                        const isCode = line.match(/^  (def |class |for |if |return |#|@|\[|\{|'|"|\d)/) || line.match(/^---/);
                        return isCode
                          ? <code key={i} style={S.inlineCode}>{line}</code>
                          : <p key={i} style={S.descLine}>{line}</p>;
                      })}
                    </div>

                    <div style={S.hintRow}>
                      <button style={{...S.hintBtn, color: section.color, borderColor: section.color + "44"}}
                        onClick={() => toggleHint(ex.id)}>
                        {hintVisible ? "🙈 Hide Hint" : "💡 Show Hint"}
                      </button>
                    </div>

                    {hintVisible && (
                      <div style={{...S.hintBox, borderColor: section.color + "66", background: section.color + "0a"}}>
                        <span style={{color: section.color}}>💡 Hint: </span>
                        {ex.hint}
                      </div>
                    )}

                    <div style={S.notesLabel}>📝 Your notes:</div>
                    <textarea
                      style={S.notesInput}
                      placeholder="Jot down your approach, questions, or observations..."
                      value={notes[ex.id] || ""}
                      onChange={e => setNotes(n => ({...n, [ex.id]: e.target.value}))}
                      rows={4}
                    />

                    <div style={S.cardFooter}>
                      <button style={{...S.doneBtn, background: isDone ? section.color : "transparent", borderColor: isDone ? section.color : "#444", color: isDone ? "#000" : "#aaa", padding: "10px 24px"}}
                        onClick={() => toggleComplete(ex.id)}>
                        {isDone ? "✓ Completed!" : "Mark as Complete"}
                      </button>
                    </div>
                  </div>
                )}
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}

const S = {
  root: { display:"flex", minHeight:"100vh", background:"#0a0a14", color:"#dde", fontFamily:"'Courier New', monospace" },
  sidebar: { width:260, background:"#0d0d1e", borderRight:"1px solid #1e1e3e", display:"flex", flexDirection:"column", flexShrink:0 },
  sideHeader: { padding:"24px 20px 16px", borderBottom:"1px solid #1e1e3e" },
  sideTitle: { fontSize:22, fontWeight:"bold", color:"#fff", letterSpacing:2 },
  sideSubtitle: { fontSize:11, color:"#555", textTransform:"uppercase", letterSpacing:2, marginBottom:16 },
  globalProgress: { display:"flex", flexDirection:"column", gap:6 },
  gpLabel: { fontSize:11, color:"#888" },
  gpBar: { height:4, background:"#1a1a2e", borderRadius:2, overflow:"hidden" },
  gpFill: { height:"100%", background:"linear-gradient(90deg,#f4a261,#2ec4b6,#9b5de5)", borderRadius:2, transition:"width 0.4s" },
  navList: { flex:1, overflowY:"auto", padding:"8px 0" },
  navItem: { width:"100%", display:"flex", alignItems:"center", gap:10, padding:"10px 16px", border:"none", borderLeft:"3px solid transparent", cursor:"pointer", textAlign:"left", transition:"all 0.2s", fontFamily:"monospace" },
  navIcon: { fontSize:18, flexShrink:0 },
  navText: { flex:1 },
  navName: { fontSize:12, fontWeight:"bold", lineHeight:1.3 },
  navCount: { fontSize:10, color:"#555", marginTop:2 },
  checkAll: { color:"#4ade80", fontSize:14 },
  main: { flex:1, overflowY:"auto", display:"flex", flexDirection:"column" },
  sectionHeader: { display:"flex", alignItems:"center", gap:16, padding:"24px 32px", borderBottom:"1px solid #1e1e3e", position:"sticky", top:0, background:"#0a0a14", zIndex:10 },
  sectionIcon: { fontSize:32 },
  sectionTitle: { fontSize:20, fontWeight:"bold" },
  sectionMeta: { fontSize:12, color:"#666", marginTop:4 },
  sectionPct: { marginLeft:"auto", fontSize:28, fontWeight:"bold" },
  exerciseList: { padding:"24px 32px", display:"flex", flexDirection:"column", gap:16 },
  exerciseCard: { borderRadius:12, overflow:"hidden", transition:"all 0.2s" },
  cardHeader: { display:"flex", alignItems:"center", justifyContent:"space-between", padding:"16px 20px", cursor:"pointer", gap:12 },
  cardLeft: { display:"flex", alignItems:"flex-start", gap:16, flex:1 },
  exNum: { fontSize:22, fontWeight:"bold", flexShrink:0, lineHeight:1 },
  exTitle: { fontSize:15, fontWeight:"bold", color:"#eee", marginBottom:8 },
  tagRow: { display:"flex", flexWrap:"wrap", gap:6 },
  diffBadge: { fontSize:10, padding:"2px 8px", borderRadius:10, fontWeight:"bold" },
  tag: { fontSize:10, padding:"2px 8px", borderRadius:10, background:"#1a1a2e", color:"#666", border:"1px solid #2a2a4e" },
  cardRight: { display:"flex", alignItems:"center", gap:12, flexShrink:0 },
  doneBtn: { padding:"6px 14px", borderRadius:8, border:"1px solid", cursor:"pointer", fontSize:12, fontWeight:"bold", transition:"all 0.2s", fontFamily:"monospace" },
  cardBody: { padding:"0 20px 20px", display:"flex", flexDirection:"column", gap:16, borderTop:"1px solid #1e1e3e", paddingTop:20 },
  descBlock: { display:"flex", flexDirection:"column", gap:2 },
  descLine: { margin:0, fontSize:14, lineHeight:1.7, color:"#ccc" },
  inlineCode: { display:"block", background:"#0a0a1a", color:"#a8ff78", padding:"2px 12px", borderRadius:4, fontSize:13, fontFamily:"monospace", margin:"1px 0", whiteSpace:"pre" },
  hintRow: { display:"flex" },
  hintBtn: { padding:"6px 14px", borderRadius:8, border:"1px solid", cursor:"pointer", fontSize:12, background:"transparent", fontFamily:"monospace" },
  hintBox: { padding:"12px 16px", borderRadius:8, border:"1px solid", fontSize:13, lineHeight:1.7, color:"#ccd" },
  notesLabel: { fontSize:11, color:"#666", textTransform:"uppercase", letterSpacing:1 },
  notesInput: { background:"#0a0a1a", border:"1px solid #2a2a4e", borderRadius:8, padding:"12px", color:"#ccc", fontSize:13, fontFamily:"monospace", resize:"vertical", lineHeight:1.6, outline:"none" },
  cardFooter: { display:"flex", justifyContent:"flex-end", paddingTop:8 }
};
