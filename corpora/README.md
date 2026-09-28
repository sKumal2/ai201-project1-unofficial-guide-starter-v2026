# The corpora

Three corpora ship with this starter for your project, plus a fourth
(`practice`) that your instructor uses in class. Pick one of the three in
Milestone 1.

They are deliberately different from each other in **shape** — how long the
documents are, and how the useful information sits inside them. That
difference is the point: the right chunk size for short posts is not the
right chunk size for long sectioned guides, and Milestone 3 is where that
starts to matter.

All three were written for this course. No real people are named.

To switch corpus, either edit `CORPUS` in `config.py`, add
`AI201_CORPUS=name` to your `.env`, or pass `--corpus name` on the command
line. Re-run `python app.py index` after switching.

## `campus_life`

**Short posts about student life at a university.** Eighty-eight documents, most of them one to three short paragraphs — the kind of thing one student writes to answer another's question. Dining halls, dorms, courses, and the administrative rules nobody explains properly. Useful information tends to sit in a single sentence.

*Pick this if* you want the closest thing to the brief's framing, and short documents where a chunk can easily hold a whole thought.

88 documents · 27,908 characters · about 317 characters per document

## `advice_threads`

**Question-and-answer threads, with several people replying.** Twenty-three threads, each with three to five replies of very uneven length, disagreeing with each other as often as not. Real answers are spread across replies rather than sitting in one place.

*Pick this if* you want messier material. Chunking is harder here — a reply boundary and a useful boundary are not the same thing — and that makes for a more interesting Milestone 3.

23 documents · 12,490 characters · about 543 characters per document

## `city_guides`

**Long structured travel guides.** Fourteen documents — nine town guides, plus five that cut across all of them (eating, walking, regional transport, seasons, accessibility). Each is one to three thousand characters, divided into labelled sections — getting there, getting around, where to eat, when to go. Information is organised by heading and spread across a paragraph rather than packed into a sentence.

*Pick this if* you want to think about splitting on structure rather than on length. Fixed-size chunks cut through these headings badly, which is exactly the problem worth solving.

14 documents · 28,958 characters · about 2,068 characters per document

## `practice`

Not for your project. This is the small corpus your instructor uses for the
in-class follow-along, kept separate so nothing done in class touches your
graded work. It's twenty-eight documents about a board game that doesn't
exist — twenty-four short ones of a paragraph or two, and four longer sectioned
guides that a fixed-size chunker cuts straight through the middle of.

28 documents · 15,901 characters · about 567 characters per document

## Bringing your own documents

You're allowed to. Make a folder at `corpora/your_name/documents/`, put
`.txt` or `.md` files in it, and point `CORPUS` at it.

Two honest warnings. You take on the cleaning work the provided corpora
already did, and it earns no extra points. And you'll need to check that
your relevance cutoff still separates in-corpus from out-of-corpus
questions, since 0.6 was chosen against these three.

That check is Milestone 4, and it is the same check that makes 0.6 a cutoff
rather than a number. Treat the default as a starting point, not an answer —
it was set against the corpora above at their shipped chunk settings, and
changing the chunking moves the distances underneath it. Measuring it
yourself is the milestone.

## Sample Chunks

Chunk 1  |  source: thread_bike_commute.txt#0  |  produced by: chunker.py::split_documents
======================================================================
THREAD: Is a bike worth it for a 20 minute walk commute?

--- reply 1 (14 votes) ---
Yeah. Cuts an 18 minute walk to about 6. The thing nobody mentions is storage — covered bike parking exists at three buildings and is full by 9amat all three.

--- reply 2 (9 votes) ---
Counterpoint, I sold mine. Between November and March the paths are either icy or salted and salt destroys a drivetrain in one season.

======================================================================
Chunk 2  |  source: thread_first_gen.txt#1  |  produced by: chunker.py::split_documents
======================================================================
--- reply 3 (16 votes) ---
Emergency fund for textbooks and travel exists and is not means-tested beyond a short form.

======================================================================
Chunk 3  |  source: thread_laptop_specs.txt#1  |  produced by: chunker.py::split_documents
======================================================================
--- reply 3 (12 votes) ---
I did two years on an 8GB machine and it was fine until the last project, at which point it very much wasn't. 16 is the answer.

======================================================================
Chunk 4  |  source: thread_office_hours_etiquette.txt#1  |  produced by: chunker.py::split_documents
======================================================================
--- reply 3 (18 votes) ---
If it helps, treat it as a standing appointment. Go every week for a month and it stops feeling like a thing.

======================================================================
Chunk 5  |  source: thread_roommate_conflict.txt#0  |  produced by: chunker.py::split_documents
======================================================================
THREAD: Roommate situation isn't working. What now?

--- reply 1 (28 votes) ---
Talk to your RA early, and frame it as 'we need help sorting this out' rather than 'move me'. Room changes are possible but the process starts with mediation and skipping that step slows it down.

--- reply 2 (14 votes) ---
Room changes happen at the semester boundary almost always, and mid-semester only in fairly serious cases.

## Test Questions

### In-Scope Questions
1. What time do dining halls close on weekends?
2. How does changing dorm rooms work?
3. Where can students study late at night?
4. What should students know about parking on campus?
5. Are students required to have a meal plan?

### Out-of-Scope Questions
1. Who won the 2026 World Cup?
2. How do I replace a car alternator?
3. What is the capital of Mongolia?
4. How do I bake a chocolate cake?
5. What is the best medication for allergies?


## Milestone 4: Relevance Cutoff

I tested five questions that should be answerable from the `campus_life` corpus and five questions that are clearly outside the corpus.

### In-Scope Results

| Question | Best Distance |
|---|---:|
| What time do dining halls close on weekends? | 0.3287 |
| How does changing dorm rooms work? | 0.5102 |
| Where can students study late at night? | 0.5500 |
| What should students know about parking on campus? | 0.6061 |
| Are students required to have a meal plan? | 0.5053 |

### Out-of-Scope Results

| Question | Best Distance |
|---|---:|
| Who won the 2026 World Cup? | 0.8564 |
| How do I replace a car alternator? | 0.8825 |
| What is the capital of Mongolia? | 0.7683 |
| How do I bake a chocolate cake? | 0.8021 |
| What is the best medication for allergies? | 0.8060 |

The highest distance among the in-scope questions was 0.6061, while the lowest distance among the out-of-scope questions was 0.7683. This created a clear gap between the two groups.

I chose a relevance cutoff of **0.68** because it falls between those values. With this cutoff, all five in-scope questions would be accepted, while all five out-of-scope questions would be rejected.

The chunks are mostly on toopic, and not just few word matches. 
The top k = 5 seems right for my retreival for now. 


## when there is no enough information: 
Question: Can freshmen park on campus for free?

Answer using only the documents above, and name the file you used.
======================================================================

I do not have enough information to answer whether freshmen can park on campus for free.

Sources retrieved: admin_parking_permits.txt, admin_wifi_and_accounts.txt, dining_verrill_street_grill.txt, money_jobs.txt, transit_shuttle.txt


## when there is enough information: 
Question: What are good dining halls?

Answer using only the documents above, and name the file you used.
======================================================================

Based on the provided documents, Pellew Dining Hall is a good choice for its dedicated allergen-free station staffed by someone who knows the menu (*dining_pellew_dining_hall.txt*). Halden Hall is also worth going to for its soup rotation and bread baked on site (*dining_halden_hall.txt*).

Sources retrieved: dining_halden_hall.txt, dining_pellew_dining_hall.txt, dining_pellew_dining_hall_followup.txt, housing_innisfree_hall.txt, housing_tamsin_court.txt

## Grounding Instruction
Question: What are good dining halls?

Answer using only the documents above, and name the file you used.
======================================================================

Based on the provided documents, Pellew Dining Hall is a good choice for its dedicated allergen-free station staffed by someone who knows the menu (*dining_pellew_dining_hall.txt*). Halden Hall is also worth going to for its soup rotation and bread baked on site (*dining_halden_hall.txt*).

Sources retrieved: dining_halden_hall.txt, dining_pellew_dining_hall.txt, dining_pellew_dining_hall_followup.txt, housing_innisfree_hall.txt, housing_tamsin_court.txt

## Where would you put the cutoff, and what would I get wrong at that number?
At a cutoff of 0.68, none of my five in-scope or five out-of-scope test questions were misclassified. The remaining risk is with borderline questions: a relevant question with an unusually high distance could be rejected, or an unrelated but semantically similar question could be accepted.


## How I used AI ?
I used AI to understand what each milestone requires us to acheive. After that, deep brainstorming and searching through the code myself, I figured out how to 
break the solution. Later, I took some help to write some readme for my project.  

Also, I asked it to tell me where would you put the cutoff, and what would I get at that number, it told me 0.68, because when I ran the function myself, and got the output threshold more than 0.6 for the chunks actually present, and 0.71 for the ones that are not. So, which is reasonable point, and I agreed to that. 

# What this does?
This project builds a RAG system, using the campus life corpus where it loads, splits into chunks, creates embeddings, and stores them in a vector db. 
Then, when a user asks a que, the prompt is compared to the chunks we created and retreives the most relevant ones. And if the questons are not close enough to the chunks we have, relevance cutoff will reject the question and return a specific prompt. But, if the chunks are found then LLM is used to give the answers only from inside the documents we have and if not enough information is found it refuses to give answer. 