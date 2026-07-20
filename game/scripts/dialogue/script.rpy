label start:

    $ renpy.music.set_volume(0.1, channel="ambient")

    stop music fadeout 0.5

    # jump day_1_school_class_physical_education
    jump day_1_school_outside

################################################################################

label day_1_school_outside:

    $ discord.update(details="In-Game", state="Outside School︳Day 1")

    play ambient bga_spring_break fadein 1
    scene bg school_outside with fade

    narrator "Today's the day. My first day at my new school, Furorida Academia."
    narrator "It feels weird not recognizing anyone around. I haven't moved to a new town in so long."
    narrator "Although... I don't really see too many people. Wonder how many students they actually have here."
    narrator "Oh well, I'd better get going. Let's check my classes."

    play sound sfx_paper_slide
    show object schedule_paper at slide_in_center

    narrator "English in Room 201, then I've got History in Room 304..."
    narrator "Hmm... these blank spots look like electives."

    play sound sfx_school_bell
    event "{b}*ring!!!* *ring!!!*{/b}"

    play sound sfx_paper_slide
    show object schedule_paper at slide_out_center

    narrator "I'll check the rest as I go... but I've got to get to class now."

    jump day_1_school_corridor_before_class_english

################################################################################

label day_1_school_corridor_before_class_english:

    $ discord.update(details="In-Game", state="In The Hallways︳Day 1")

    play ambient bga_school_chatter fadein 1 fadeout 1
    scene bg school_corridor with fade

    narrator "Where is this class?"
    narrator "I'm on the right floor..."

    play sound sfx_paper_slide
    show object schedule_paper at slide_in_center

    narrator "Room 201... 201..."
    narrator "Oh, found it!"

    play sound sfx_paper_slide
    show object schedule_paper at slide_out_center

    narrator "I think I'm late on the first day..."
    narrator "Oh well, I'm sure they aren't too harsh about it."
    narrator "Time to go in."

    jump day_1_school_class_english

################################################################################

label day_1_school_class_english:

    $ discord.update(details="In-Game", state="English Class︳Day 1")

    play ambient bga_room_noise fadein 1 fadeout 1
    scene bg school_classroom_english with fade

    show teacher_jackson at left, fade_in

    teacher_jackson "Everybody late coming in, pick a seat and sit down. We'll have seating charts done by the end of the day, so it doesn't matter where you sit right now."
    teacher_jackson "I don't want anyone messing around, so please sit still and listen."
    teacher_jackson "My name is Mr. Jackson, and I'll be your English teacher for this year."
    teacher_jackson "I've been teaching this class for six years now, so I've seen it all. Don't think you can get anything past me."
    teacher_jackson "Outside of class, I have a wife and two kids, and a very well-behaved pitbull named Pinky."
    teacher_jackson "My wife's a laundry attendant at the hotel around here, and before I became a teacher, I was a proofreader."
    teacher_jackson "I reviewed documents and articles for spelling and grammar errors. So fun stuff, right?"
    teacher_jackson "Anyway, you've gotten to know a bit about me, so now it's time for me to get to know a bit about you."
    teacher_jackson "Everyone will raise their hand one by one, state their name, and share a fun fact about themselves."
    teacher_jackson "You, the late kid. You'll go first. Give me your name and a fact about yourself."

    $ _raw = renpy.input("{i}What's my name?{/i}", length=24, allow="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'. ").strip()
    $ var_string_playername = _raw.title() if _raw else "Player"

    player "I'm [var_string_playername]. I just moved into town, and this is my first year here."
    player "For a fun fact, I uh... play video games in my free time."
    player "...That's about it."
    teacher_jackson "...Very unique. And just moved into town too..."
    teacher_jackson "Furorida doesn't often see new people coming in. I'm... sure you'll enjoy it."
    teacher_jackson "Anyway, next... Do we have an Edward here? Edward Harrington?"

    show edward at right, fade_in

    edward "Oi' teach, quit playin' wit me. I'm present!"
    edward "I'm from Hertfordshire, that's Britain bruv. I transferred 'ere just two years ago. I'm also a thug so don't be playin' wit me. You 'ear mates?"
    edward "Me, I'm gon' be your top student, y'hear?"
    teacher_jackson "Fascinating... You sound delightful. Everybody say hello to Edward."
    event "..."

    show edward at right, fade_out

    teacher_jackson "Okay... next up is Jesse. Jesse Heart, what's your fun fact?"

    show jesse at right, fade_in

    jesse "H-hey guys. I'm Jesse... {i}{color=#5b5b5b}{size=26}as the teacher said...{/size}{/color}{/i}"
    jesse "Fun fact... I stopped the great alien space heist of {i}{color=#5b5b5b}{size=26}...this year...{/size}{/color}{/i}"
    jesse "And I've also founded a social c-club and we're on our way to proving that the earth is flat!"
    jesse "But my parents told me I needed to go to a r-real school instead of homeschool, so now I'm h-here..."
    teacher_jackson "I get that you want to be the class clown, Jesse, but can we get a real fact about you?"
    jesse "What?! W-Which part isn't real?"
    teacher_jackson "I see... Well, next we have Cameron. Cameron Mann."
    jesse "Y-you didn't answer my question!"

    show jesse at right, fade_out

    teacher_jackson "Cameron, you're up."

    show cameron at right, fade_in

    $ var_integer_randomroll = renpy.random.randint(1, 100)

    if var_integer_randomroll <= 99:
        cameron "I'm here. My name's Cameron, I'm a third-year student, and a fun fact about me is that I'm great at photography."
    else:
        cameron "I'm tung tung tung sa'here. My name's Cameron, I'm a third-year student, and a fun fact about me is that I'm great at photography."

    cameron "I enjoy taking photographs of the school and the surrounding outdoor area. But really, I want to become an actor one day."
    teacher_jackson "{i}{color=#5b5b5b}{size=26}...Not with that stupid name you won't...{/size}{/color}{/i}"
    teacher_jackson "I can't wait to retire so I never have to hear you speak one more word, Cameron."
    cameron "Yes, teach."

    show cameron at right, fade_out

    teacher_jackson "Alright, who's up next? Faith! Faith Walker?"

    show faith at right, fade_in

    faith "I'm here! Or uh... present!"
    teacher_jackson "And your fun fact?"
    faith "Um... My name is Faith. I used to spend time working on a farm."
    faith "Originally, I'm from Tennessee. Kingsport, Tennessee."
    teacher_jackson "Can't say I know anything about Kingsport or Tennessee."
    teacher_jackson "Is that all?"
    faith "Yeah, I think so?"
    teacher_jackson "What a striking bunch we have this year."

    show faith at right, fade_out

    teacher_jackson "Surprisingly, there are more of you than last year..."
    teacher_jackson "While I'm working on getting the syllabus ready, talk amongst yourselves."

    show teacher_jackson at left, fade_out

    narrator "...That was interesting..."
    narrator "Can't say I have any plans to get to know these people anytime soon."
    narrator "Just gotta get through the year. No trouble involved."

    show cameron at right, fade_in

    cameron "{i}{color=#5b5b5b}{size=26}Pssst... Stranger...{/size}{/color}{/i}"
    player "Wh- Huh?"
    cameron "My apologies. But your name was [var_string_playername], right?"
    player "Yeah, that's me."
    cameron "Greetings then, [var_string_playername]. And welcome to Furorida Academia. As you heard earlier, my name is Cameron."
    cameron "I'm kind of the unofficial school guide."
    cameron "If you need anything, just ask me and I'll have the answer."
    player "Right then... How come Mr. Jackson seems to hate you?"
    cameron "Well, I don't have {i}all{/i} the answers. It sounds like he just hates my name. It's funny at this point."
    player "Weird..."
    cameron "Yeah... but who isn't weird here?"
    player "Oh, so everyone here is like this?"
    player "Like... awkward, eccentric, quirky?"
    cameron "You catch on quick. Just try to make some friends and you'll get through it just fine."
    player "I kind of went in here planning to do the opposite."

    show teacher_jackson at left, fade_in
    
    teacher_jackson "Alright, everybody pay attention!"
    cameron "Well, good luck with that... I'll see you around. Just come to me if you need anything."

    show cameron at right, fade_out

    teacher_jackson "Let's test the overall class intelligence level before we get into any actual material."
    teacher_jackson "I need a few volunteers to answer some questions for me."

    show faith at right, fade_in

    faith "We're doing work on the first day?"
    teacher_jackson "Yes...? What, do you all want to gather in a circle and toss a ball?"
    faith "...No..."

    show faith at right, fade_out

    teacher_jackson "Then let's begin, shall we? Raise your hand to volunteer!"
    event "..."
    teacher_jackson "If no one raises their hand, I'm going to start calling out names."
    event "..."
    teacher_jackson "Jesse! Answer this question for me."

    show jesse at center, fade_in

    jesse "What!? What do you want from me?"
    teacher_jackson "I want you to answer a question."
    jesse "Oh, w-what is it?"
    teacher_jackson "Jesse, what is a noun?"

    show edward at right, fade_in

    edward "Oi', wh' kind of school is this, mate?"
    teacher_jackson "Just let Jesse answer the question."
    jesse "I-I don't know! No idea!"

    show cameron at right, fade_in
    show edward at right, fade_out

    cameron "You don't know what a noun is?"
    jesse "N-no! I b-bet you couldn't answer it either...!"
    teacher_jackson "Terrific... So it'll be like teaching last year then."

    show edward at right, fade_in
    show cameron at right, fade_out
    show jesse at center, fade_out

    edward "Y'idiot, mate! Just let me answer, ol'right?"
    teacher_jackson "Sure, Edward. What is a noun?"
    edward "A noun is..."
    edward "Y'ought to use it in a sentence first, yeah?"
    teacher_jackson "Certainly. The sentence will be... \"Edward, what is a noun?\""
    edward "Well... bloody hell mate, never mind if you're just gon' be playin' wit' me then."
    teacher_jackson "Spectacular."

    show edward at right, fade_out

    teacher_jackson "I can't wait to teach you all for the rest of this school year."
    teacher_jackson "You all seem bright and intelligent. Full of creativity..."

    show cameron at right, fade_in

    cameron "Excuse me, Mr. Jackson, may I answer the question?"
    teacher_jackson "Cameron, do I have to send you to the principal's office?"
    cameron "No, teach."

    show cameron at right, fade_out

    teacher_jackson "Alright then. Now it's time to start the seating charts."
    teacher_jackson "I get that you're all probably upset about wanting to sit with your friends and all."
    narrator "..."
    teacher_jackson "But we need these charts to ensure the class stays civil and focused... or whatever these charts do."
    teacher_jackson "Jesse, you'll be sitting next to Edward, front row."
    teacher_jackson "[var_string_playername], you'll be sitting next to Cameron, middle row."
    teacher_jackson "And Faith, you'll be sitting at the back."

    show faith at right, fade_in

    faith "Usually I'd be upset about that, but... thank god."

    show edward at center, fade_in

    edward "I've gotta be put with this kid? Oi', you better be quiet, yeah?"

    show jesse at right, fade_in
    show faith at right, fade_out

    jesse "A-are you talking to me?"
    edward "Yeah, who else, mate?"

    show cameron at right, fade_in
    show edward at center, fade_out
    show jesse at center, fade_out

    cameron "I'm good with this seating. Right, [var_string_playername]?"
    player "Yeah, sure."
    cameron "Sounds good then."
    teacher_jackson "Tomorrow I expect everybody to have the class materials listed."

    play sound sfx_school_bell
    event "{b}*ring!!!* *ring!!!*{/b}"

    teacher_jackson "Alright, get to your next class! I'll see you all tomorrow."
    cameron "See you later, [var_string_playername]."

    show cameron at right, fade_out

    jump day_1_school_corridor_before_class_history

################################################################################

label day_1_school_corridor_before_class_history:

    $ discord.update(details="In-Game", state="In The Hallways︳Day 1")

    play ambient bga_school_chatter fadein 1 fadeout 1
    scene bg school_corridor with fade

    narrator "Glad that's over with..."
    narrator "Not glad that I'll have to deal with that every day though."
    narrator "Anyways, where am I going again?"

    play sound sfx_paper_slide
    show object schedule_paper at slide_in_center

    narrator "Room 304, right."

    play sound sfx_paper_slide
    show object schedule_paper at slide_out_center

    narrator "Looks like this is the place."

    jump day_1_school_class_history

################################################################################

label day_1_school_class_history:

    $ discord.update(details="In-Game", state="History Class︳Day 1")

    play ambient bga_room_noise fadein 1 fadeout 1
    scene bg school_classroom_history with fade

    teacher_moore "Greetings everybody!"
    teacher_moore "I'm your rad history teacher! Ready to teach you all about the coolness of history!"
    narrator "...What."
    teacher_moore "Welcome, welcome! Before we get into our lesson, I notice some new faces around here."
    teacher_moore "For our first day, we'll all be sitting in a circle and passing a ball around."
    teacher_moore "Once you catch the ball, you'll tell us your name and a fact about history."
    narrator "Great..."
    teacher_moore "Everybody sit down, sit down!"
    teacher_moore "Now here's the ball, it's printed to look like a globe, see?"
    teacher_moore "July, you'll go first."
    teacher_moore "Catch!"

    play sound sfx_ball_catch_swoosh

    july "My name's July, and uh... history is a very important subject to learn in school!"
    teacher_moore "So it is! Pass it on!"

    play sound sfx_ball_falling_swoosh

    avery "...I'm... Ah!"
    avery "Sorry... I missed."
    teacher_moore "All good, try again!"
    avery "I got it...!"

    play sound sfx_ball_falling_swoosh

    avery "...Oops... sorry again."
    teacher_moore "One more time!"

    play sound sfx_ball_catch_swoosh

    avery "...There...! I'm Avery, and uh... the oldest known love poem was found dating back to two thousand BCE."
    teacher_moore "Fascinating! Next!"

    play sound sfx_ball_catch_swoosh

    luthor "It's Luthor."
    teacher_moore "...And your fact?"
    luthor "I dunno."
    teacher_moore "C'mon, you can think of something!"
    luthor "..."
    teacher_moore "Disappointing! Keep on thinking while we continue!"
    teacher_moore "You're up!"

    play sound sfx_ball_catch_swoosh

    player "I'm [var_string_playername], and... George Washington was the president once."
    teacher_moore "Correct! He was!"
    teacher_moore "...I have one more student on my roster but they don't seem to be here..."
    teacher_moore "Peculiar... Oh well!"
    teacher_moore "Everybody move the chairs over and sit down! It's time to get into our lesson!"
    teacher_moore "Today, we'll be discussing the War of 1812."
    teacher_moore "Can anyone guess which year it happened?"
    event "..."
    july "1812...?"
    teacher_moore "Exactly! Now can you tell me why it happened?"
    event "..."
    teacher_moore "No one? Well, it was a war fought between the US and Britain."
    teacher_moore "Does that give anyone an idea?"
    event "..."
    teacher_moore "It was a conflict caused by Britain encroaching on the United States' trade routes."
    luthor "Man, who cares about this? This sucks."
    teacher_moore "What do you mean, Luthor? This war was very impactful to the history of the United States."
    teacher_moore "Do you {i}really{/i} know what sucks? The economy."
    teacher_moore "If America didn't fight back, they might have lost their economic rights!"
    teacher_moore "How would you feel if someone took {i}your{/i} wallet away and told you that you couldn't have it back?"
    teacher_moore "They had to fight back against the British!"
    teacher_moore "And fighting against the British is what the States does best!"
    teacher_moore "Take the Revolutionary War for example..."
    teacher_moore "Where would they be without that?"
    teacher_moore "Where would {i}we{/i} be without that?"
    narrator "...I think I'm starting to zone out..."
    narrator "This guy sure does love his history."
    narrator "Maybe a little too much."
    july "Heya, neighbor!"
    player "Huh, me?"
    july "Yeah, since we have some time, I think it'd be best to get to know each other right now."
    july "I'm July. And you're [var_string_playername], right?"
    player "Yeah."
    july "He does this a lot, by the way."
    july "It's unfortunate that you ended up here. Not the greatest way to start your first day..."
    player "What do you mean?"
    july "The teacher. He loves to ramble on about history... it gives us essentially a free class period."
    july "But if you ask me, it just shows how qualified he is to teach this class."
    player "Not if he argues with the class the entire period..."
    teacher_moore "And that's why the Seven Years' War caused Britain to shoot themselves in the foot, so to speak."
    teacher_moore "Great Scott! Class is nearly over!"
    teacher_moore "Pack up, everybody! We'll finish this up next class period."
    july "Looks like he's done for now..."
    july "Come find me during lunch and I can show you around the place."
    july "You'll grow to love it here. It just takes a little time."

    play sound sfx_school_bell
    event "{b}*ring!!!* *ring!!!*{/b}"

    july "See you around!"
    narrator "A tour around the school... maybe I should go."
    narrator "..."

    play sound sfx_books_falling
    player "Whoa!" with hpunch

    avery "My books!"
    avery "Ah, I'm sorry..."
    player "Don't apologize! It was my fault. I'll help you pick them up."
    avery "Oh, no it's fine...!"
    avery "Um, you're [var_string_playername], right? The new student?"
    player "That's me."
    avery "Oh, that's cool."
    avery "You... wouldn't happen to like poetry, would you?"
    player "Poetry...?"

    menu:
        narrator "How should I respond?"

        "Yeah, I like poetry.":
            $ var_boolean_likespoetry = True
            player "Yeah, I like poetry."
            avery "That's great!"

        "It's not really my thing.":
            $ var_boolean_likespoetry = False
            player "It's not really my thing."
            avery "Oh, I see."

    avery "Wait, where are my manners...!"
    avery "I'm Avery."
    avery "I'm... kind of the head of the Poetry Club."

    if var_boolean_likespoetry:
        avery "We're always looking for new members. No pressure, of course."
        avery "Or... if you could tell others about the club, that would help us out greatly."
    else:
        avery "If you could tell others about the club, that would help us out greatly."

    avery "Gosh, look at the time!"
    avery "I've gotta get going..."

    if var_boolean_likespoetry:
        avery "I'd better be seeing you at the next club meeting, okay?"
    else:
        avery "If you change your mind... I'd better be seeing you at the next club meeting, okay?"

    avery "If not, I know where you have second period."
    player "Uhh..."
    avery "Kidding! It's a joke!"
    avery "Seriously though, consider it."

    if var_boolean_likespoetry:
        avery "I'll be seeing you... hopefully."
    else:
        avery "Hopefully I'll be seeing you..."

    narrator "Poetry, huh."
    narrator "Didn't know that was an option. Now I do."
    narrator "Anyways, it's lunch time now right?"
    narrator "Should probably start heading over."

    jump day_1_school_lunch

################################################################################

# label day_1_school_corridor_before_lunch:

#     $ discord.update(details="In-Game", state="In The Hallways︳Day 1")

#     play ambient bga_school_chatter fadein 1 fadeout 1
#     scene bg school_corridor with fade

################################################################################

label day_1_school_lunch:

    $ discord.update(details="In-Game", state="At Lunch︳Day 1")

    play ambient bga_school_chatter fadein 1 fadeout 1
    scene bg school_cafeteria with fade

    narrator "Time to get a meal."

    scene bg school_cafeteria_line with fade

    narrator "Let's see what they sell here."
    narrator "..."
    narrator "There's way too much to choose from."
    narrator "What even is a pineapple turkey burger?"
    narrator "Hmm..."
    narrator "I have to decide fast."
    narrator "I guess you can't go wrong with a... uh..."
    teacher_warmuth "Ahem!"
    player "Oh, sorry."
    teacher_warmuth "Welcome to the Furorida Cafe. What will you be having today?"
    player "Uh..."
    player "Let me get, uh..."
    teacher_warmuth "Come on, order something."
    player "A salad!"
    player "Yeah, a salad..."
    teacher_warmuth "Alrighty, one salad coming up."
    teacher_warmuth "What dressing would you like with that?"

    menu:
        narrator "Which dressing do I want?"

        "Ranch Dressing":
            $ var_string_saladdressing = "ranch"
            player "I'll take ranch."
            teacher_warmuth "Ranch, good choice."

        "Italian Dressing":
            $ var_string_saladdressing = "italian"
            player "Italian please."
            teacher_warmuth "Italian it is."

    teacher_warmuth "Would you like to add on a drink with that?"
    player "No thank you."
    teacher_warmuth "Okay, just one salad."

    $ var_integer_randomroll = renpy.random.randint(1, 100)

    if var_integer_randomroll <= 99:
        teacher_warmuth "Your total will be $9.56."
    else:
        teacher_warmuth "Your total will be $9.67."

    teacher_warmuth "Will you be paying with cash or card today?"
    player "Total...? Paying...?"
    player "I uh, don't have my wallet."
    teacher_warmuth "That's okay, do you have tap-to-pay on your phone?"
    player "Tap-to-pay?"
    player "I think I do."
    teacher_warmuth "Great, just tap your phone when you're ready."
    event "..."
    teacher_warmuth "I'm sorry, your card declined."
    teacher_warmuth "You are welcome to tap again."
    narrator "Declined? I guess I'm short on money..."
    player "It's fine. You can cancel the order."
    teacher_warmuth "Well in that case, you can check out the room next door."
    teacher_warmuth "Our food pantry offers free food to students who need it."
    narrator "Free?"
    narrator "I guess it doesn't hurt to check it out."
    player "Thanks. I'll check it out."
    chris "{i}{color=#5b5b5b}{size=26}Man, did I just hear a card decline?{/size}{/color}{/i}"

    scene bg school_cafeteria_pantry with fade

    narrator "These food options aren't exactly the greatest thing around."
    narrator "I'm pretty sure this beef jerky is expired..."
    narrator "But it's free, so I'll take what I can get."
    narrator "I guess a jerky stick and a bottle of water is nutritional enough..."

    scene bg school_cafeteria with fade

    narrator "I suppose this counts as lunch..."

    menu:
        narrator "Now where should I sit?"

        "I'll sit with July.":
            $ var_string_lunchtable = "july"
            narrator "I think I'll sit with July."
            narrator "Gotta find where July is sitting..."

        "By myself.":
            $ var_string_lunchtable = "myself"
            narrator "I'll just sit by myself for now."
            narrator "I'll find a place."

    narrator "Hmm..."

    play sound sfx_carton_drop

    narrator "Oops."
    narrator "Dropped my water, I'll just pick that right up..."

    play sound sfx_whistle
    event "{i}*whistle!*{/i}" with vpunch

    narrator "What now...?"
    locke_hall_monitor "HEY YOU! PUT YOUR HANDS WHERE I CAN SEE THEM!"
    player "What do you want?"
    locke_hall_monitor "Do you realize that you just LITTERED?"
    player "Really...? Is this about my water?"
    player "I was just picking it up..."
    locke_hall_monitor "Don't play dumb with me, you know your CRIMES!"
    player "Crimes...? This is stupid."
    locke_hall_monitor "GASP! Profanity too!"
    locke_hall_monitor "The staff are going to have a field day with you."
    player "C'mon man, it's my first day."
    locke_hall_monitor "Oh. Well in that case, you're free to go."
    player "...Really?"
    locke_hall_monitor "Yeah."
    locke_hall_monitor "They don't talk about the rules until the assembly tomorrow."
    player "Assembly?"
    locke_hall_monitor "Yeah, the assembly! Everybody has to go."
    player "Didn't hear about this."
    locke_hall_monitor "Figures, too busy breaking rules to go?"
    locke_hall_monitor "Well, gotta blast! Remember to never-ever litter!"
    narrator "Guess I'm going to an assembly tomorrow..."
    narrator "Anyways, let's find that seat."

    if var_string_lunchtable == "july":
        jump day_1_school_lunch_table_july

    elif var_string_lunchtable == "myself":
        jump day_1_school_lunch_table_myself

################################################################################

label day_1_school_lunch_table_july:

    $ discord.update(details="In-Game", state="At Lunch︳Day 1")

    july "Hey, [var_string_playername]! Over here!"
    player "Oh, hey July."
    july "What'd you get?"
    player "I just got a jerky stick and some water."
    july "Nice, kinda... I got a turkey sandwich."
    july "Glad you found your way through the cafeteria here."
    player "Is it normally a challenge?"
    july "Was it not one for you?"
    player "Well, actually I guess it was."
    july "Locke totally stopped you, didn't he?"
    player "Is that his name?"
    july "The hall monitor, yeah."
    july "He'll find the smallest reasons to stop you."
    july "Not sure why though, he's not getting paid for it or anything."
    july "But uh, he's not actually all that bad if you get to know him."
    player "Really..."
    july "Yeah, he's friends with a lot of the students here."
    player "Surprising... Anyways, we have an assembly tomorrow?"
    july "Yep! They'll ramble on about school spirit and rules for about an hour."
    july "But after that, you'll get to choose your electives."
    july "Have you decided what you're gonna pick?"
    player "I haven't really thought about that yet."
    july "I'm doing band, have been for years."
    july "You could join that, do you play any instruments?"
    player "Tried, never been good at one."
    july "Maybe band'll be a good excuse to learn one then."
    july "...Unless you wanna sing, like I am."
    player "Yeah I'll pass on the singing."
    player "I'll think about band though. I don't really know the other options."
    july "I think there's Art, Culinary, Film, and Spanish? ...At least available to us right now."
    july "Oh, and yeah, band too. Obviously."
    player "Doesn't sound like a lot."
    july "Don't think the school's budget's a lot, so."
    player "That explains the lunch then."
    july "Uh, yeah. That jerky is probably expired."
    player "Oh I know."
    july "Think lunch is about to end, catch you later?"
    player "Yeah, I'll see you around."

    play sound sfx_school_bell
    event "{b}*ring!!!* *ring!!!*{/b}"

    narrator "Huh, right on time..."
    narrator "I didn't really end up eating my lunch... At least it was free though."

    play sound sfx_paper_slide
    show object schedule_paper at slide_in_center

    narrator "Well, where am I going next?"
    narrator "P.E.? Right after lunch?"

    play sound sfx_paper_slide
    show object schedule_paper at slide_out_center

    narrator "Oh well... I'm headed to the gym."

    jump day_1_school_corridor_before_class_physical_education

################################################################################

label day_1_school_lunch_table_myself:

    narrator "Nobody's over here."
    narrator "Guess I can take this seat for now..."
    narrator "Finally have some peace..."
    chris "HEY MR. BROBROKESTER."
    chris "Gimme your lunch money."
    narrator "...Is he talking to me?"
    chris "I KNOW YOU CAN HEAR ME ROBBING YOU!"
    player "Hey uh, sir?"
    player "You know I have nothing to give, right?"
    chris "I HEARD YOUR BROKE ASS GOT YOUR CARD DECLINED."
    player "Yeah... so what exactly can I give to you?"
    chris "LUNCH, MONEY."
    player "Right, uh."
    player "...And if I don't have any money?"
    chris "YOU WILL PAY WITH..."
    chris "...Can I have that?"
    player "Come on man, this is my only food."
    player "If you're hungry, just say so."
    chris "Sorry, I don't speak broke."
    chris "Just give me the food, and all is forgiven."
    player "What is forgiven?"
    chris "...Being broke."
    player "You know what? Fine, take it."
    chris "Thank you for your cooperation."
    event "..."
    chris "This food sucks."
    chris "Do better next time! I'm throwing this out."
    player "..."
    player "Please tell me lunch is over soon."
    chris "Hmm? What was that? BROKIE!"
    player "Nothing..."

    play sound sfx_school_bell
    event "{b}*ring!!!* *ring!!!*{/b}"

    narrator "Finally..."

    play sound sfx_paper_slide
    show object schedule_paper at slide_in_center

    narrator "Where to now?"
    narrator "P.E.? Great..."

    play sound sfx_paper_slide
    show object schedule_paper at slide_out_center

    narrator "Guess I'm headed to the gym."

    jump day_1_school_corridor_before_class_physical_education

################################################################################

label day_1_school_corridor_before_class_physical_education:

    $ discord.update(details="In-Game", state="In The Hallways︳Day 1")

    play ambient bga_school_chatter fadein 1 fadeout 1
    scene bg school_corridor with fade

    narrator "Sucks the gym is all the way on the other side of the building."
    narrator "At least it'll burn off the lunch a bit."
    narrator "I think I'm here."

################################################################################

label day_1_school_class_physical_education:

    $ discord.update(details="In-Game", state="In P.E. Class︳Day 1")

    play ambient bga_room_noise fadein 1
    scene bg school_track with fade

    teacher_galloni "Everybody get in line! Single file!"
    teacher_galloni "It's time for roll call!"
    luthor "What, is this a prison or something?"
    teacher_galloni "Funny one here, you're going first."
    teacher_galloni "Raise your hand high, and say present!"
    luthor "Oh well, present."
    teacher_galloni "...We'll work on it. Let's see who else is here."
    teacher_galloni "[var_string_playername]?"
    player "Present!"
    teacher_galloni "And Randy?"
    randy "Here coach!"
    teacher_galloni "You're supposed to say present."
    randy "Oh uh... present!"
    teacher_galloni "Chris!"
    chris "Sir yes sir! Present!"
    luthor "{i}{color=#5b5b5b}{size=26}Suck up...{/size}{/color}{/i}"
    chris "What'd you say to me, buddy?"
    chris "Don't make me take your lunch money..."
    luthor "We just had lunch."
    chris "...Don't make me take your gym money."
    luthor "Yeah, okay..."
    teacher_galloni "Quiet down, Quiet down! We're not finished."
    teacher_galloni "Last one, don't mess this up!"
    teacher_galloni "Sienna!"
    event "..."
    teacher_galloni "Sienna Rivera!"
    sienna "Yeah whatever. Uh, present."
    teacher_galloni "Okay... I don't want to make this tough for you all, especially on the first day."
    teacher_galloni "But this, is not acceptable!"
    teacher_galloni "Everybody needs to fall in line!"
    teacher_galloni "We're gonna be running around this gym, no slacking!"
    teacher_galloni "Let me get my stopwatch..."
    luthor "Wait a minute."
    luthor "Why is this class so much smaller than the others?"
    chris "They told me this was the gifted class."
    sienna "..."
    sienna "You're joking right?"
    chris "Would I ever lie to you?"
    randy "Coach... Is he telling the truth?"
    teacher_galloni "No, no, Chris, why would you tell them that?"
    teacher_galloni "Just because of that, Randy has to run first."
    randy "B-but..."
    teacher_galloni "GO!"
    randy "Yes sir!"
    luthor "..."
    luthor "At least I'm not going first anymore."
    luthor "Gives me more time to warm up!"
    chris "Too bad I am the fastest runner there is!!!"
    chris "I'm gonna run sooo much faster than you."
    chris "I'm a fast, speedy, quick guy. You're a slow, slow, slow guy."
    teacher_galloni "Alright, since you two can't shut your mouths! You two are going next!"
    teacher_galloni "Luthor, next! Then Chris."
    luthor "..."
    luthor "Dammit..."
    event "..."
    player "Crazy people, right...?"
    sienna "Are you... talking to me?"
    player "I guess."
    sienna "Yeah, don't."
    player "Okay then..."

    if var_string_lunchtable == "july":
        narrator "So much for that."
        randy "Ignore her, she can be like that sometimes."
        sienna "I can hear you, 'Ice Cream for Breakfast.'"
        randy "See."

    elif var_string_lunchtable == "myself":
        chris "Aww... Did brokesph get rejected?"
        player "Is this all you do?"
        randy "Ignore those two, they can be a handful."

    player "Oh, hey."
    randy "You new here? Glad to meet ya, I'm Randy."
    randy "And your name was [var_string_playername], right?"
    player "Yeah."
    player "Quick question?"
    randy "Shoot."
    player "How did you run the mile that fast?"
    randy "Oh... right."
    randy "Coach doesn't keep track."
    randy "You could go up there and say 13 seconds and he'll put that down."
    randy "I still try a lap at least once."
    randy "But man, do I hate running."
    chris "Oh, I wonder why."
    chris "Some kind of... issue?"
    chris "Some kind of... respiratory issue?"
    randy "I mean... yeah."
    chris "That's a good excuse."
    chris "I just leave after my second lap."
    sienna "Do you ever stop talking?"
    chris "Sienna, you're a... "
    chris "... Huh..."
    chris "...Damn."
    chris "You got me there."
    teacher_galloni "Chris, you're up!"
    chris "But it's that other guy's turn..."
    teacher_galloni "Chris! Go... NOW!!!"
    chris "Ughhhh! Fine!"
    chris "This isn't over!"
    luthor "Did he notice me?"
    narrator "Was he hiding behind the bleachers?"
    sienna "Coach!"
    luthor "Shut up, Sienna!"
    sienna "Or else what!?"
    luthor "Or else I'll have your Chemistry partner be Cameron."
    sienna "Fine."
    sienna "Stupid TA."
    luthor "What was that?"
    sienna "Wasn't talking to you!"
    sienna "Umm..."
    sienna "I was talking to them."
    narrator "Is she looking at me?"
    sienna "You gonna help me out or what?"

    menu:
        narrator "Should I help her?"

        "Help Sienna":
            $ var_boolean_helpedsienna = True
            player "So, uh..."
            player "Did you do the homework for math?"
            sienna "Oh."
            sienna "Yeah, what about it?"
            player "I just needed help with..."
            player "Question 2."
            sienna "Oh that!"
            sienna "I, um, guessed."
            sienna "You're on your own."
            player "I can probably just put down random numbers."
            sienna "*chuckles*"
            sienna "Yeah, that is true."
            teacher_galloni "Sienna, your turn!"
            sienna "Damn it."
            sienna "I guess I have to get running." 
            sienna "I hope I helped at least a little bit."

        "Ignore Sienna":
            $ var_boolean_helpedsienna = False
            narrator "I think I'll look the other way."
            player "You know this floor looks really shiny."
            luthor "Not even the new person wants to talk to you!"
            luthor "Talk again and I'll change the seats."
            narrator "I look over at Sienna."
            player "Does a TA have that kind of power?"
            sienna "Don't talk to me."
            sienna "Don't even look at me."
            teacher_galloni "Sienna, your turn!"
            narrator "Sienna quickly got up and went straight to the track."
            narrator "I think I made a mistake."
            narrator "I might be able to make it up with her."

    play sound sfx_school_bell
    event "{b}*ring!!!* *ring!!!*{/b}"

    teacher_galloni "What! Huh!"
    teacher_galloni "Looks like class is over."
    teacher_galloni "Everyone who ran, give me your times."
    teacher_galloni "The rest of you will finish up tomorrow."
    narrator "Gym could either make or break my whole year here."
    narrator "Let's hope I get some fun out of it."
    
    if var_boolean_helpedsienna == True:
        sienna "Thanks for having my back today."
        sienna "It's good to know that there's one sane person in this class."
        player "Any time!"

    narrator "I finally get a break."
    narrator "For today, at least."
    narrator "What to do with all this free time."
    
    jump day_1_school_corridor_before_class_science

################################################################################

label day_1_school_corridor_before_class_science:

    $ discord.update(details="In-Game", state="In The Hallway︳Day 1")

    play ambient bga_school_chatter fadein 1 fadeout 1
    scene bg school_corridor with fade

    narrator "I left the gym and went to go explore the campus a bit more."
    narrator "But there is just one problem."
    narrator "I think I'm lost."
    player "I was like, 90 percent sure my science class was over here."
    player "Did I make a wrong turn?"
    jimmy "You look lost."
    jimmy "Do you need some help?"
    player "Oh, yeah, actually."
    player "I'm looking for my science class."
    player "It's my sixth period, but I don't want to be late on my first day."
    jimmy "First day! In that case, hi..."
    jimmy "I'm Jimmy!"
    jimmy "Nice to meet you."
    player "I'm [var_string_playername]."
    jimmy "You said you are looking for a science class?"
    player "Correct."
    player "Mr. Moon's class."
    jimmy "Mr. Moon, huh?"
    jimmy "He's a bit more down the way you came in."
    jimmy "Room 181."
    player "Thank you so much."
    jimmy "No problem."
    jimmy "Always here to help."
    jimmy "Say, you don't have an elective either, do you?"
    player "Yeah, how'd you know?"
    jimmy "I don't have one picked out either."
    jimmy "You have a good excuse with this being your first day and all."
    jimmy "I can't make up my mind."
    jimmy "But tomorrow is the day we have to pick one."
    player "Tomorrow?"
    jimmy "Yeah."
    jimmy "Did they not tell you?"
    player "No."
    jimmy "Well, you better start thinking."

    play sound sfx_school_bell
    event "{b}*ring!!!* *ring!!!*{/b}"

    jimmy "Looks like class has started for everyone else."
    jimmy "I for one need to study."
    jimmy "So I'll be catching you on the flip side."
    jimmy "I hope you have a great time here."
    
    narrator "Jimmy left the hallway."
    narrator "Now my break starts."
    narrator "I suppose it wouldn't hurt to explore electives before tomorrow comes by."

    jump day_1_school_class_break

################################################################################

label day_1_school_class_break:

    $ discord.update(details="In-Game", state="On Break︳Day 1")

    play ambient bga_school_chatter fadein 1 fadeout 1
    scene bg school_corridor with fade

    narrator "Now my science class is down there..."
    narrator "But there are more classes I can check out."
    narrator "I don't have time to check every class."

    menu:
        narrator "Which way should I go?"

        "North":
            $ var_string_breakdirection = "north"
            jump day_1_school_class_break_direction_north

        "East":
            $ var_string_breakdirection = "east"
            narrator "There's gotta be something over here."
            jump day_1_school_class_break_direction_east

        "West":
            $ var_string_breakdirection = "west"
            narrator "West it is."
            jump day_1_school_class_break_direction_west

################################################################################

label day_1_school_class_break_direction_north:

    play ambient bga_school_chatter fadein 1 fadeout 1
    scene bg school_corridor_art with fade

    narrator "This way."
    narrator "Everything on that wall is bright"
    narrator "Is this an art class?"
    locke "Are you in this class too?"
    player "Hmm?"
    player "No."
    player "Just looking around."
    locke "If you aren't in this class..."
    locke "Then why aren't you in a class?"
    locke "Are you..."
    locke "*gasp*"
    locke "ARE YOU DITCHING!?"
    player "Oh, no, nothing like that."
    player "Like I told you before, it's my first day."
    player "Just looking at classes before I pick one."
    locke "In that case, you can join art."
    locke "Art is super duper fun!"
    locke "Although, I am not the bestest artist, I try my best."
    player "Art, huh."
    player "What exactly do you do in this class?"
    locke "Oh, we do everything."
    locke "Like a whole ton of cool stuff."
    locke "Last week we attempted paper mache."
    locke "I made this really cool bowl."
    locke "It was like..."
    locke "Bowl sized!"
    locke "And then we uhh... We draw."
    locke "We draw like a lot!"
    locke "I like drawing cats."
    locke "Maybe you should join my class. There's so many cool people there."
    locke "Tell me, tell me, please."
    locke "Will you sign up?"
    player "We'll see. I'm still checking on my options."
    locke "Okay."
    locke "Art is really fun!"
    locke "I hope I will see you tomorrow."
    locke "My water break is over so I have to head back."
    locke "We are doing water coloring today!"
    narrator "..."
    narrator "Art class... I could use the creativity."

    play sound sfx_school_bell
    event "{b}*ring!!!* *ring!!!*{/b}"

    narrator "Looks like my break is over. At least I know where to go for science now."

    jump day_1_school_class_science

################################################################################

label day_1_school_class_break_direction_east:

    play ambient bga_school_chatter fadein 1 fadeout 1
    scene bg school_corridor_culinary with fade

    narrator "I smell something"
    narrator "I can't tell what it is"
    narrator "but it smells amazing"

    if var_boolean_helpedsienna == True:
        sienna "What brings you around here stranger?"
        player "Hmm?"
        sienna "Hey, its me..."
        sienna "again"
        player "Oh! hello Sienna"
        sienna "You're not skipping class are you"
        sienna "pretty risky for your first day"
        player "I'm just looking around for an elective"
        sienna "You don't have one yet?"
        sienna "The school made me pick mine like..."
        sienna "a semester ago"
        player "Well it is my first day here."
        player "that kind of changes things"
        sienna "Oh yeah... thats right"
        sienna "anyways what brings you out here?"
        sienna "Thinking about taking the culinary class?"
        player "I mean..."
        player "Maybe."
        player "Its an option for right now"
        sienna "Cooking is a good skill."
        sienna "plus what I make here saves me from having to buy lunch the next day."
        player "Is the school okay with letting you guys handle cooking equipment on your own?"
        sienna "Yeah."
        sienna "Its our own fault if we end up burning ourselves"
        sienna "Cooking has rules you need to follow"
        sienna "You may get away with not following it for a little bit"
        sienna "Then a little oil splash reminds you why those rules exist in the first place"
        player "That seems... Dangerous"
        sienna "Its a little dangerous when you're starting out"
        sienna "but it beats spending 20 dollars a meal somewhere else."
        player "True, money can be low at times"
        sienna "See!"
        sienna "I think everyone should take this class"
        sienna "I would much rather learn a life skill than learn something like the clarinet"
        sienna "especially in that band class"
        sienna "Trust me."
        sienna "There are some stuck up people in there."
        
        # play sound sfx_phone_alarm

        sienna "Oh, thats my alarm"
        sienna "I gotta go check up on my dish"
        sienna "It was good seeing you"
        sienna "oh, one more thing."
        sienna "I better see you in this class tomorrow."
        narrator "Sienna headed back to the class"

    elif var_boolean_helpedsienna == False:
        player "It looks like theres a whole kitchen in there"
        player "despite the low number of students everyone is working hard on their own thing."
        player "Its good to know there is a cooking class here."
        narrator "Someone from inside the classroom notices you from the window"
        sienna "Hey Mrs Campbell."
        sienna "There's a creep spying on us through the window"
        player "uh oh"
        player "I think I have to run before I get caught"

        menu:
            narrator "Which way do I run?"

            "North":
                $ var_string_breakdirection = "north"
                jump day_1_school_class_break_direction_north

            "West":
                $ var_string_breakdirection = "west"
                jump day_1_school_class_break_direction_west

################################################################################

label day_1_school_class_break_direction_west:

    play ambient bga_school_chatter fadein 1 fadeout 1
    scene bg school_corridor_band with fade

    narrator "Am I hearing music? Maybe there's an elective over here..."

    # play sound sfx_distant_singing

    narrator "Is that, singing...?"
    narrator "I think it was over there by the window. I hope they don't mind an audience..."
    narrator "..."
    laine "Do you mind?"
    player "Oh, I uhh... I just wanted to say it sounded great."
    laine "Oh, I know. But I wouldn't say great."
    laine "I'd say perfect."
    player "I guess, yeah."
    laine "Oh no, you wouldn't get it. You don't seem like someone with a knack for music."
    laine "I've never seen you around the music class."
    laine "As a matter of fact, I've never seen you at all."
    laine "Not that I care, but are you new?"
    player "Yeah, actually, it's my first day."
    laine "Well, in that case, it's never too late to join the class."
    laine "If you thought my singing was... how did you put it?"
    laine "'Great'."
    laine "You could hear more of it if you signed up."
    laine "If you have the talent for it, that is. Music isn't for everyone, after all."
    player "Yeah... great."
    laine "Do you think you're talented enough to join the likes of me?"
    player "You'll find out tomorrow."
    laine "Hmm? Well, I better see you tomorrow."
    laine "Or else, I'll think very little of you..."
    laine "Not like I already do, but you get the picture."
    player "Uh huh..."
    laine "Well, I better get back to my class."
    laine "We have a performance soon, and of course, they need me."
    laine "You better be here tomorrow."
    laine "...Whoever you are."
    narrator "She doesn't seem like the nicest person to talk to."
    narrator "But it seems she wants people to join."
    narrator "Just... could have phrased it a little more kindly."

    play sound sfx_school_bell
    event "{b}*ring!!!* *ring!!!*{/b}"

    narrator "Looks like my break is over. At least I know where to go for science now."

    jump day_1_school_class_science

################################################################################

label day_1_school_class_science:

    $ discord.update(details="In-Game", state="On Break︳Day 1")

    play ambient bga_school_chatter fadein 1 fadeout 1
    scene bg school_classroom_science with fade
    
    teacher_moon "Come in everybody, come in!"
    teacher_moon "Have a seat everyone, any seat at all."
    teacher_moon "Hope you all are ready for some science, because we're gonna get right into that."
    teacher_moon "But first of all, attendance."
    teacher_moon "Is [var_string_playername] here?"
    player "Right here."
    teacher_moon "Next up on the list is Jake! Jake Glue!"
    jake "I'm present! Or... I was present, but that was in the past."
    teacher_moon "Good one Jake! You're the glue that holds my classroom together."
    teacher_moon "Now we have Locke?"
    locke "Present! Wait, presents? Is it Christmas already?"
    narrator "Oh great, the hall monitor is in here."
    teacher_moon "Sure is, Locke! Now is Jesse here?"
    jesse "R-Right here, Mr. Moon!"
    teacher_moon "And last but not least, Faith! Faith Walker."
    faith "Over here!"
    teacher_moon "Great, everyone's here!"
    teacher_moon "Now, before we get into all the fun and interesting science..."
    teacher_moon "We first need to talk about the importance of lab safety!"
    teacher_moon "We have goggles and gloves in the cabinets to the right of the class, next to the windows."
    teacher_moon "And while you all should be careful enough to never have to use it, we have an eye wash station in the corner."
    teacher_moon "As well as a shower area next to it. With some curtains for privacy."
    jesse "You m-mean if we get something on us, we have to get into a s-shower... {i}{color=#5b5b5b}{size=26}in front of the entire class?{/size}{/color}{/i}"
    teacher_moon "Yes, but there are curtains! And it's only if you get some really dangerous stuff on you!"
    teacher_moon "Now does everyone understand our lab safety?"
    faith "Sure... I think."
    jake "You know it, Mr. Moon!"
    teacher_moon "Now, let's begin."
    teacher_moon "I need three groups of two, so everyone form a group!"
    jake "But Mr. Moon, you have five students!"
    teacher_moon "Darn, you're right. Come work with me, Jake!"
    jake "Coming right away!"
    narrator "A group of two... hm."
    narrator "Faith seems like a safe choice..."
    narrator "But July did say Locke wasn't all that bad..."
    narrator "And uhh... Jesse, is something."

    menu:
        narrator "Who do I pick to be my science partner?"

        "Faith":
            $ var_string_sciencepartner = "faith"
            narrator "I'll pick Faith."
            player "Hey Faith, wanna group up?"
            faith "Sure! Don't really know anyone here any better anyways..."
            player "Yeah... I'm still getting used to it."
            player "Anyways, uh... Mr. Moon!"
            teacher_moon "Yes, [var_string_playername]?"
            player "Me and Faith are grouping up."
            teacher_moon "Perfect! I assume that means Locke and Jesse are grouping up as well?"
            jesse "G-guess so then..."

        "Locke":
            $ var_string_sciencepartner = "locke"
            narrator "I'll see if I can come around to Locke."
            player "Hey uh, Locke? Wanna be science partners?"
            locke "Really!! AWESOME SAUCE!!!"
            locke "Yes siree! Mr. Moon! Me and..."
            player "It's [var_string_playername]."
            locke "Me and [var_string_playername] are science partners!"
            teacher_moon "Fantastic you two!"
            jesse "I g-guess me and Faith are grouping up then."

        "Jesse":
            $ var_string_sciencepartner = "jesse"
            narrator "Well, let's try Jesse."
            player "Hey Jesse?"
            jesse "Y-yeah? What do you need?"
            player "Wanna group up for this?"
            jesse "I g-guess I have to."
            teacher_moon "Jesse, are you grouping up with [var_string_playername]?"
            jesse "Yeah..."
            teacher_moon "Alright, that means Faith and Locke are grouping up I assume?"
            faith "Guess so...!"

    teacher_moon "Then everyone's decided! Let's get to the lesson now."
    teacher_moon "So, each group is going to get a bottle of soda, and we're gonna put some mentos into it!"
    teacher_moon "So, come up here and grab your bottle."
    jake "And then whats after the mentos? Do we calculate anything?"
    teacher_moon "Of course not! Now come on ahead!"
    narrator "Sounds like this won't be too bad."
    
    if var_string_sciencepartner == "faith":
        player "I'll go get the bottle and mentos, I guess."
        faith "Alright."
        narrator "..."
        player "I'm here."
        teacher_moon "Here you go! Be careful with it!"
        teacher_moon "Don't want to see it explode early! Right?"
        narrator "...I'm starting to question how qualified each of these teachers really are..."
        player "Alright, I got it."
        faith "Great. Now uh... now what?"
        faith "Do we just... start already?"
        player "I have no idea... No need to rush it, I think..."
        faith "Sure. So, uhh.. what do you... think so far?"
        player "Of, what exactly?"
        faith "The whole place really, the school... the people..."
        faith "I'm... having a hard time looking forward to this place."
        faith "Everyone here, is a lot different than the people over at where I come from..."
        faith "Actually, everything here is a lot different. Not just the people..."
        faith "Maybe, I just miss it?"
        player "Oh right, you're from like, the country?"
        faith "If that's how you wanna put it..."
        player "Wish I could say I relate, moved around so much I don't really get attached."
        player "Don't know, if it's a curse or a blessing really."
        faith "Sounds like a blessing to me."
        player ""

    elif var_string_sciencepartner == "locke":
        locke "I'll get the stuff!"
        player "Sure..."
        
    elif var_string_sciencepartner == "jesse":
        jesse "You... should probably go get the bottle and s-stuff."
        player "Alright then..."
        narrator "..."
        player "I'm here."
        teacher_moon "Here you go! Be careful with it!"
        teacher_moon "Don't want to see it explode early! Right?"
        narrator "...I'm starting to question how qualified each of these teachers really are..."

################################################################################

label end:

    return