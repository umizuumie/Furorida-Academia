label start:

    $ renpy.music.set_volume(0.1, channel="ambient")

    stop music fadeout 0.5

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
    $ var_string_player_name = _raw.title() if _raw else "Player"

    player "I'm [var_string_player_name]. I just moved into town, and this is my first year here."
    player "For a fun fact, I uh... play video games in my free time."
    player "...That's about it."
    teacher_jackson "Very unique. And just moved into town too..."
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

    $ var_integer_random_roll = renpy.random.randint(1, 100)

    if var_integer_random_roll <= 99:
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
    cameron "My apologies. But your name was [var_string_player_name], right?"
    player "Yeah, that's me."
    cameron "Greetings then, [var_string_player_name]. And welcome to Furorida Academia. As you heard earlier, my name is Cameron."
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
    teacher_jackson "[var_string_player_name], you'll be sitting next to Cameron, middle row."
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

    cameron "I'm good with this seating. Right, [var_string_player_name]?"
    player "Yeah, sure."
    cameron "Sounds good then."
    teacher_jackson "Tomorrow I expect everybody to have the class materials listed."

    play sound sfx_school_bell
    event "{b}*ring!!!* *ring!!!*{/b}"

    teacher_jackson "Alright, get to your next class! I'll see you all tomorrow."
    cameron "See you later, [var_string_player_name]."

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

    player "I'm [var_string_player_name], and... George Washington was the president once."
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
    july "I'm July. And you're [var_string_player_name], right?"
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
    avery "Um, you're [var_string_player_name], right? The new student?"
    player "That's me."
    avery "Oh, that's cool."
    avery "You... wouldn't happen to like poetry, would you?"
    player "Poetry...?"

    menu:
        narrator "How should I respond?"

        "Yeah, I like poetry.":
            $ var_boolean_likes_poetry = True
            player "Yeah, I like poetry."
            avery "That's great!"

        "It's not really my thing.":
            $ var_boolean_likes_poetry = False
            player "It's not really my thing."
            avery "Oh, I see."

    avery "Wait, where are my manners...!"
    avery "I'm Avery."
    avery "I'm... kind of the head of the Poetry Club."

    if var_boolean_likes_poetry:
        avery "We're always looking for new members. No pressure, of course."
        avery "Or... if you could tell others about the club, that would help us out greatly."
    else:
        avery "If you could tell others about the club, that would help us out greatly."

    avery "Gosh, look at the time!"
    avery "I've gotta get going..."

    if var_boolean_likes_poetry:
        avery "I'd better be seeing you at the next club meeting, okay?"
    else:
        avery "If you change your mind... I'd better be seeing you at the next club meeting, okay?"

    avery "If not, I know where you have second period."
    player "Uhh..."
    avery "Kidding! It's a joke!"
    avery "Seriously though, consider it."

    if var_boolean_likes_poetry:
        avery "I'll be seeing you... hopefully."
    else:
        avery "Hopefully I'll be seeing you..."

    narrator "Poetry, huh."
    narrator "Didn't know that was an option. Now I do."
    narrator "Anyways, it's lunch time."

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

    narrator "Lunch, time to get a meal."

    scene bg school_cafeteria_line with fade

    narrator "Let's see what they sell here."
    narrator "..."
    narrator "There's way too much to choose from."
    narrator "What even is a pineapple turkey burger?"
    narrator "Hmm..."
    narrator "I have to decide fast."
    narrator "I guess you can't go wrong with a..."
    narrator "Uh..."
    teacher_warmuth "Ahem!"
    player "Oh!"
    teacher_warmuth "Welcome to the Furorida Cafe. What will you be having today?"
    player "Uh..."
    player "Let me get, uh..."
    teacher_warmuth "Come on, order something."
    player "A salad!"
    player "Yeah, a salad."
    teacher_warmuth "Alrighty, one salad coming up."
    teacher_warmuth "What dressing would you like with that?"
    
    menu:
            narrator "Which dressing do I want?"

            "Ranch Dressing":
                $ var_string_salad_dressing = "ranch"
                player "I'll take ranch."
                
            "Italian Dressing":
                $ var_string_salad_dressing = "italian"
                player "Italian please."

    if var_string_salad_dressing == "ranch":
        teacher_warmuth "Ranch, good choice."
        
    elif var_string_salad_dressing == "italian":
        teacher_warmuth "Italian it is."

    teacher_warmuth "Would you like to add on a drink with that?" 
    player "No thank you."
    teacher_warmuth "Okay, one salad." 

    $ var_integer_random_roll = renpy.random.randint(1, 100)

    if var_integer_random_roll <= 99:
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
                $ var_string_lunch_table = "july"
                narrator "I think I'll sit with July."
                narrator "Gotta find where July is sitting..."
                
            "By myself.":
                $ var_string_lunch_table = "myself"
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

    if var_string_lunch_table == "july":
        jump day_1_school_lunch_table_july

    elif var_string_lunch_table == "myself":
        jump day_1_school_lunch_table_myself

################################################################################

label day_1_school_lunch_table_july:

    $ discord.update(details="In-Game", state="At Lunch︳Day 1")

    play ambient bga_school_chatter fadein 1 fadeout 1
    scene bg school_cafeteria with fade

    july "Hey, [var_string_player_name]! Over here!"
    player "Oh, hey July."
    july "What'd you get?"
    player "I just got a jerky stick and some water."
    july "I just got a turkey sandwich."
    july "Glad you found your way through the cafeteria here."
    player "Is it normally a challenge?"
    july "Was it not one for you?"
    player "Well, actually I guess it was."
    july "Locke totally stopped you, didn't he."
    player "Is that his name?"
    july "The hall monitor, yeah."
    july "He'll find the smallest reasons to stop you."
    july "Not sure why though, he's not getting paid for it or anything."
    july "But uh, he's not actually all that bad if you get to meet him."
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
    july "I think there's Art, Culinary, Film, and Spanish? At least available to us right now."
    july "Oh, and yeah, band too. Obviously."
    player "Doesn't sound like a lot."
    july "Don't think the school's budget's a lot, so."
    player "That explains the lunch then."
    july "Uh, yeah. That jerky is probably expired."
    player "Oh I know..."
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

    $ discord.update(details="In-Game", state="At Lunch︳Day 1")

    play ambient bga_school_chatter fadein 1 fadeout 1
    scene bg school_cafeteria with fade

    narrator "Nobody's over here."
    narrator "Guess I can take this seat for now..."
    narrator "Finally have some peace..."
    chris "HEY MR. BROBROKESTER."
    chris "Gimme your lunch money."
    narrator "Is he talking to me?"
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

    player "Finally..."
    player "Where to now?"

    play sound sfx_paper_slide
    show object schedule_paper at slide_in_center
 
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

################################################################################

label day_1_school_class_physical_education:

    $ discord.update(details="In-Game", state="In P.E. Class︳Day 1")

    play ambient bga_spring_break fadein 1
    scene bg school_track with fade

################################################################################

label end:

    return
