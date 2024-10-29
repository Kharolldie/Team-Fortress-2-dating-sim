
define p = Character("Miss Pauling", color="#a425b4", image='pauling')
define a = Character("Miss Ahmavaara", color="#5f00a3")
define t = Character("The tank operator", color="#97b7c6", image='tank')
define q = Character("???", color="#ffffffff")
define scout = Character("Scout", color="#97b7c6")
define admin = Character("Administrator", color="#4b00ad")


label start:

menu:
    "Chapter 1":
        jump chapter1

    "Chapter 2":
        jump chapter2

    "Chapter 3":
        jump chapter3

    "Chapter 4":
        jump chapter4

    "Chapter 5":
        jump chapter5

label chapter1:

    scene hallway with fade

    "Today is the first day in my new workplace. Miss Pauling, who I've met just five minutes ago, is taking me to meet the mercenaries."

    show pauling neutral
    p "Are you nervous, Miss Ahmavaara? I know you've just been kinda kidnapped, put in a new uniform, met me and now you have to meet nine more people, but this will be the least stressful day you'll have from now on."
   
    p sad "Sorry to be this depressing from the start. But Administrator expects a lot from both of us."

    a "I did sign up for this."

    p neutral "You're right."

    show pauling at left 
    with easeinright
    p "Oh! We're here!"

    "The hallway has led us to a door. Ruckus can be heard behind it. I resist the urge to roll my eyes and sigh in discomfort in front of Miss Pauling. She opens the door and the racket of grown men fills my eardrums."
    hide pauling

    scene conference room with fade
    show engineer sad
    q "C'mon, fellas. Shut up!"
    hide engineer
    q "I WILL SHUT A BOX WITH YOUR ASS IN IT AND KICK IT DOWN THE STAIRS!"
    show heavy angry with vpunch
    q "SHUT MOUTHS!!!"
    hide heavy
    "The whole room becomes dead silent thanks to this guy. Thank God there's someone tolerable in this team."

    show pauling neutral with moveinleft
    p "I've gathered you all here to introduce you my new colleague Miss Ahmavaara."

    a "Pleasure to be working with you."

    hide pauling
    "Someone made an audible gasp. Each of the men turned around to look at the guy sitting in the very back row. They looked at him surprised. Like it would be the 7th miracle of the blonde guy in the back to make any noices."
    
    show tank embarrassed
    q "..."

    "He seemed to regret drawing attention to him. He looked at me again."

    q "You’re Finnish?"

    "I could tell from his rally English alone he was one too."
    hide tank
    menu:

        "Yes.":
            jump choice1_yes

        "I will not disclose personal information.":
            jump choice1_i_will_not

        "Why are you asking?":
            jump choise1_why

    return

    label choice1_yes:
        show tank happy
        q "Me too!"
        show tank embarrassed
        q "Anyway… Go on. I’ll stop talking."
        hide tank

        jump choice1_done

    label choice1_i_will_not:
        show tank sad
        q "Sorry."

        "He looks at the floor and stops the interruption."
        hide tank

        jump choice1_done

    label choise1_why:
        show tank embarrassed
        q "Just curious."

        "I can tell he’d give a longer and detailed explanation why if he wasn’t under eleven people’s curious eyes."
        hide tank

    label choice1_done:

        "I was introduced and the men were told I would be doing half of Miss Pauling’s work. I would be in contact to them every now and then."
        show scout angry
        "The youngest of the lot voiced his complaints about that. I already dislike him…"
        hide scout
        scene hallway with fade
        "The conference was over and I started walking away from the room with Miss Pauling as the men were getting up from their chairs."

        "My name is called behind us. The speaker translated my title into my native language."
        show tank neutral
        q "Neiti Ahmavaara?"

        "Miss Pauling and my eyes were round out of surprise. This man probably came to tell me something he was too shy to say at the conference now that we were alone. -Almost alone."
        
        show pauling at left: 
            pos (0.0, 0.2) anchor (0.0, 0.0)

        p doubt "Would you like to speak with him alone?"
        hide pauling
        hide tank
    menu:

        "Yes.":
            jump choice2_yes
        
        "I’d prefer if you stayed with me.":
            jump choice2_id_prefer



    label choice2_yes:
        show pauling neutral
        p "All right. I’ll wait for you by the exit."
        hide pauling with dissolve

        "She starts walking away."

        show tank doubt
        q "..."

        "The moustache man watches carefully as the rest of the mercenaries walk past us. Some of them walked slowly on purpose in case they could hear what he was about to say."
        "When he made sure they were far enough, he spoke to me in Finnish."

        show tank happy
        q "Tereve, tereve! Mie halusin vaa sannoo, et on tosi mukava, et täälo toone suamalaine. Voiv vihroin puhhuu ommaa äirinkiältä."

        "I squint my eyes as if that’d help me understand his God forsaken dialect. I reply with proper finnish."

        a "(Please speak in written language. I don’t understand a single word you’re saying.)"

        show tank surprised
        q "(Oh! I’m sorry. Is this better?)"

        a "(Yes. Now start over, please.)"

        show tank happy
        q "(I said I just wanted to say it’s so nice that there’s another Finn. I can finally speak my native language.)"

        a "(Don’t get too used to it. We won’t be talking that much.)"

        show tank neutral
        q "(I know. You’ll be really busy.)"
    
        show tank happy
        q "(I’m the Tank operator by the way. You can call me Tank like everyone does.)"

        "He offers me his hand. I shake it. It’s hot and a tad sweaty."

        a "(You probably won’t need another introduction from me?)"

        show tank
        t happy "(No. I already remember your name better than my colleagues’.)"

        "I raise my brows at him."

        t neutral "(You must be busy. I just wanted to introduce myself and tell you how happy I am that you’re here. I’ll talk to you later, allright?)"

        a "(Mhm.)"

        hide tank with dissolve
        "I watched quietly as he walked away."
        "I walked to the exit and met up with Miss Pauling. I’m relieved she didn’t look curious."

        jump choice2_done


    label choice2_id_prefer:

        show pauling neutral
        p "Okay."
        
        show pauling at left:
            pos (0.0, 0.2) anchor (0.0, 0.0)

        show tank embarrassed
        "I’m sure the man wanted to talk to me alone since he doesn’t seem to like audience. But I need to follow Miss Pauling. I would be lost in the building and didn’t know where to go next if she left."

        hide pauling

        show tank doubt
        q "..."

        "The moustache man watches carefully as the rest of the mercenaries walk past us. Some of them walked slowly on purpose in case they could hear what he was about to say."
        "When he made sure they were far enough, he spoke to me in Finnish."

        show tank happy
        q "Tereve, tereve! Mie halluusin vaa sannoo, et on tosi mukava, et täälo toone suamalaane. Voiv vihroin puhhuu ommaa äirinkiältä."

        "I squint my eyes as if that’d help me understand his God forsaken dialect. I reply with proper finnish."

        a "(Please speak in written language. I don’t understand a single word you’re saying.)"

        show tank surprised
        q "(Oh! I’m sorry. Is this better?)"

        a "(Yes. Now start over, please.)"

        show tank happy
        q "(I said I just wanted to say it’s so nice that there’s another Finn. I can finally speak my native language.)"

        a "(Don’t get too used to it. We won’t be talking that much.)"

        show tank neutral
        q "(I know. You’ll be really busy.)"
    
        show tank happy
        q "(I’m the Tank operator by the way. You can call me Tank like everyone does.)"

        "He offers me his hand. I shake it. It’s hot and a tad sweaty."

        a "(You probably won’t need another introduction from me?)"

        show tank
        t happy "(No. I already remember your name better than my colleagues’.)"

        "I raise my brows at him."

        t neutral "(You must be busy. I just wanted to introduce myself and tell you how happy I am that you’re here. I’ll talk to you later, allright?)"

        a "(Mhm.)"
        
        hide tank with dissolve
        "Miss Pauling and I watched quietly as he walked away. I’m relieved my female colleague didn’t look curious."


        jump choice2_done

    label choice2_done:
        show pauling neutral
        p "Ready to continue? Good."
        hide pauling with dissolve
        "We exit the building together. Now that the mercenaries know I exist, it was time for me to learn the timetables, tech and maps."
    
        scene black with dissolve
        jump chapter2
        return

label chapter2:

    "Chapter 2"

    scene hallway
    "Miss Pauling and my steps echo in the empty hallway. We aren’t saying a word as we’re walking to the office she told me about."
    "She and I will spend most of our work hours in there. This will be my first time stepping in our office."
    "She probably has her mind in her other work-related things as she’s showing me around. I am not speaking simply because I am not told to, I hate small talk and because I don’t have any questions."
    "Honestly I don’t think I’d speak up even if I had any questions either… That’s a bad habit I need to get rid of. This job is important."
    "Miss Pauling and I stop in front of a lift. She presses a button and the doors open before us."
    scene lift

    show pauling neutral at left with moveinleft
    p "Our office is pretty high up. The view is nice."
    a "Allright."
    hide pauling

    scene office
    "After a little wait, the lift doors open and we’re greeted with a cozy atmosphere. Wooden furniture, dim lightning, windows to look outside."

    show pauling happy
    p "I ordered you your very own work desk. I put it next to mine."
    p embarrassed "We can … put it elsewhere if you wanna work in your own space."
    hide pauling

    menu:
        "Its current location is fine":
            jump current_location_is_fine

        "I wanna have a little space.":
            jump i_wanna_have_space

    return

    label current_location_is_fine:

    show pauling happy
    p "Ah! Brilliant! Saves us time not needing to move it."
    p neutral "Let’s get straight to work shall we?"
    hide pauling

    jump choice3_done

    return

    label i_wanna_have_space:

    show pauling neutral
    p "I totally understand. Please help me move your desk."
    p "I’ll grab this end. You’ll grab the other."

    "I obey. We move my desk across the room. I will be working our backs facing each other."

    p "“Phew! Now we can get to work.”"
    hide pauling

    jump choice3_done

    return

    label choice3_done:

    "Miss Pauling carries a large pile of papers to me tells me to organise in chronological order. I eye the familiar typewriter font in the paper on top of the pile before setting it on my desk."
    "My eyes became tired as the hours went by."
    "I completed the sorting after a couple of more hours."
    a "I’m done."
    show pauling doubt
    p "Just a second."
    p neutral "There."
    p "Good job. I’m gonna take those from you and put them in folders. You can take a little break."

    show pauling surprised at left
    "She walked a few steps away from me with the pile. Her face lit up and she turned around."

    p "There’s the mercenaries’ files in the 3rd locker of my desk. You can get to know the boys a little better by reading them."
    p embarrassed "Some of their backgrounds may be a little weird. But you won’t mind, will you?"
    a "At least it’ll be an interesting legible."
    p neutral "You’re right. I’ll go now. See you soon."

    "She presses the lift button with her elbow and leaves when the doors open. I’m surprised how easy she made carrying the papers look."
    hide pauling with moveoutleft

    "I stand up and rummage through the 3rd locker of Miss Pauling’s desk. I get my hands on a folder titled as the mercenaries’ files. It says “CLASSIFIED” in red on the middle."
    "My lips curl into a smile as I walk to my own desk. The classified text made the folder look very secret and important. I’m excited I have a pass that lets me get away with something a normal civilian wouldn’t."
    "A normal citizen would probably get assassinated for this."
    "I sat down, crossed my legs and prepared to dive into the mysteries of the folder. Which one should I read first?"

    default Demoman = False
    default Pyro = False

    menu:
        "Medic":
            jump Medic
            
        "Scout":
            jump Scout

        "Heavy":
                jump Heavy

        "Sniper":
            jump Sniper

        "Spy":
            jump Spy
            
        "Soldier":
            jump Soldier
            
        "Demoman":
            $ Demoman = True
            jump Demoman

        "Pyro":
            $ Pyro = True
            jump Pyro
            
        "Engineer":
            jump Engineer

    return

    label Medic:

    "I picked the BLU team doctor’s file first. It had the Medic’s black and white picture. He looked serious."

    a "{i}Oh. His real name is Ludwig. Hm. He definitely looks like a Ludwig.{/i}"
    "There was age, height, weight and other medical information. Now came the exciting part. -His background."
    "…"
    "I blink and re-read the text in case my eyes were deceiving me the first time."
    "I chuckle out loud. No way this guy’s background is like a horror-themed sitcom."
    "I doubted if Medic’s qualified to be the team’s healer but I guess he is since he’s not been fired yet. He also did invent a ray that heals people in a short moment and a way to make them invincible for 8 seconds."
    "On second thought I wouldn’t fire him either. Even though he should’ve been locked up in an asylum 30 years ago…"
    jump file_choice_done
    return

    label Scout:
    "I picked the BLU team Scout’s file first. It had his black and white picture. He’s smiling."
    "This is the guy who complained about me being here."

    a "{i}Oh. His real name is Jeremy.{/i}"
    "There was age, height, weight and other medical information. Now came the exciting part. -His background."
    "The craziest part of his background is he having seven brothers. Oh, the poor mother of his not only gave birth but raised eight Scouts."
    jump file_choice_done
    return

    label Heavy:
    "I picked the BLU team’s Heavy weapons guy’s file first. It had his black and white picture. He looked serious."
    a "{i}Oh. His real name is Mikhail. That’s such a nice name. Gives me sympathetic vibes.{/i}"
    "There was age, height, weight and other medical information. Now came the exciting part. -His background."
    a "{i}He’s from the USSR. That makes us neighbours.{/i}"
    "I can’t lie his story wasn’t exciting but it did make me frown."
    "I read the current description of him. It says he usually shows clear signs of enjoyment such as laughing when shooting people down. In addition, he treats his minigun as if it was sentient."
    "I shrug. I’m not weirded out by that. Good for him."
    jump file_choice_done
    return

    label Sniper:
    "I picked the BLU team Sniper’s file first. It had his black and white picture. He looked serious."
    a "{i}His real name is mister Mundy, I see…{/i}"
    "…"
    "Hmm. This one’s nothing crazy. An assassin so good at his job that even Admin became interested in hiring him."
    "I wonder why Miss Pauling warned me. Maybe the rest of the mercenaries are more mental."
    jump file_choice_done 
    return

    label Spy:
    "I picked the BLU team Spy’s file first. It had his black and white picture. He looked serious and wealthy type of guy."
    "His first and surname was stated but I don’t know how to pronounce them."
    "French is such a weird language compared to my own where every letter is pronounced the way it’s written and doesn’t play mind games like English and especially French."
    "There was age, height, weight and other medical information. Now came the exciting part. -His background."
    "Before I opened the Spy’s file, I had expected something crazy like Miss Pauling warned. He was just a hitman so good that even Admin became interested in hiring him."
    "I wonder why Miss Pauling warned me. Maybe the rest of the mercenaries are more mental."
    jump file_choice_done
    return

    label Soldier:
    "I picked the BLU team Soldier’s file first. It had his black and white picture. He was doing a salute with a serious face."
    "He’s chosen “Jane Doe” as his alias. I raise my brows confused."
    "An unidentifiable woman as an alias? Why? Maybe the rest of the file gives me an explanation."
    "There was his first and surname, age, height, weight and other medical information. Now came the exciting part. -His background."
    "…"
    "After reading the text I stare at it blankly. I shake my head and rub my temples processing all the information I just read with the two of my eyes."
    "Jesus Christ…"
    "I can see why Miss Pauling warned me before leaving."
    "I’m entertained by utterly mental stories but this one left me speechless."
    a "{i}All right… Let’s see the rest.{/i}"
    jump file_choice_done
    return

    label Demoman:
    "I picked the BLU team Demoman’s file first. It had his black and white picture. He looked sleepy."
    a "{i}Tavish Finnegan DeGroot. This is the first time hearing any of those names.{/i}"
    "Even though his first name was unfamiliar to me, it did amuse me. “Tavish” means a very normal or basic person in Finnish."
    "I’m hoping this coincidence isn’t foreshadowing anything."
    "The file had also stated his age, height, weight and other medical information. Now came the exciting part. -His background."
    "…"
    "I squint my eyes in disbelief. This text wants me to believe his eye is cursed by magic."
    "I need to ask Miss Pauling about this."
    jump file_choice_done
    return

    label Pyro:
    "I picked the BLU team Pyromaniac’s file first. It had the Pyro’s black and white picture."
    "There was age, height, weight and other medical information."
    a "{i}“First name: Unknown. Surname: Unknown.” How mysterious.{/i}"
    a "{i}“The subject has a neurological developmental disability: Semi-verbal autism.”{/i}"
    "That explains his muffling."
    "Now came the exciting part. -His background."
    "…"
    "The text and the evidence pictures gave me chills."
    "The burned victims had a terrified expressions plastered on their faces forever. Their skin was crusty and blackened."
    "The Pyro was known to show clear signs of enjoyment such as laughing and happily hopping around when burning people alive."
    "This guy is definitely a sadist."
    jump file_choice_done
    return

    label Engineer:
    "I picked the BLU team Engineer’s file first. It had his black and white picture. He was smiling with teeth."
    a "{i}Dell Conagher’s his real name.{/i}"
    a "{i}Dell… Dell… That’s such a nice name. No K’s or R’s or any other letters that make names sound blunt or harsh. “Dell” is perfectly soft.{/i}"
    a "{i}I have been wondering what to name my future cat or chihuahua. Now I know. If I ever get a pet that is…{/i}"
    "There was age, height, weight and other medical information. Now came the exciting part. -His background."
    "I was highly impressed until the Gunslinger part."
    "Why the hell would one replace their fully functioning hand -and even the right one- for a robotic one?"
    "I shrug. He’s the one with 11 PhDs. Not me. Maybe he’s onto something. I really hope so for his sake…"
    jump file_choice_done
    return

    label file_choice_done:
    
    if Pyro:

        "I read more files. The stories got crazier and crazier. I admit I was very entertained so far."
        "I was surprised the Pyro being the only one whose real name was a mystery."
    else:
        "I read more files. The stories got crazier and crazier. I admit I was very entertained so far."
        
    "Now was the last file’s turn. The tank operator’s."
    a "{i}This is the guy who was a little too excited to see me. For a Finn too… Let’s see what’s this guy’s deal.{/i}"
    "I go through the text in a calm manner. I slowly start glaring at the text, scrunching up my nose and tightening my grip."
    "What a nutcase!"
    "I’m getting goosebumps. I was careful not to damage the paper even though I wanted to. I want nothing to do with anything regarding to this man."
    jump chapter3
    return
  
label chapter3:
    scene black
    "Chapter 3"

    scene office
    "I carefully close the folder and stood up. I held it far away from me as if it was contaminated and put it back where I took it from."
    "The bell of the lift played a tune and I see Miss Pauling."
    show pauling neutral with moveinleft
    p "Follow me. I’ll show you to the dorms."
    "I’m positively surprised there being dorm rooms. She kept the lift doors open for me as I stepped it."
    scene lift
    show pauling neutral 
    p "We can both go to sleep earlier than I’d normally go."
    "“Earlier” she said. It’s 2 o’ clock in the morning."
    "The improvement of Miss Pauling’s sleep schedule makes me feel more appreciated to be here."

    if Demoman:
        "Demoman’s file still bugged me. I had to ask about that."
        a "Miss Pauling?"
        p "Yes?"
        a "Demoman’s file said his eye was cursed by magic. Is that really the case?"
        p happy "Heh! That must’ve been a surprise."
        p neutral "Yes, that’s true. Magic is real. Every Halloween a wizard, a giant Demoman’s eye, a pumpkin head with an axe, etcetera etcetera comes to kill the mercenaries."
        "I stare at Miss Pauling not saying a word, my mouth left open a little bit."
        p happy "Don’t worry! You and I don’t have to deal with any of them. All those anomalies only try to kill the mercenaries."
        a "Sorry. I just can’t believe magic is real."
        "I hold my temple. My brain felt heavy. I was mindblown."
        p neutral "Isn’t the old, red-wearing man who flies with reindeer during the Christmas nights from your country?"
        a "That’s just a cultural hoax parents tell their kids to make them behave."
        "Miss Pauling smirked at me coyly."
        p happy "Or is he…?"
        a "…"
        a "I don’t know. Maybe Santa is real after all."
        jump no_demoman
    
    
    label no_demoman:
        scene dorm with fade  
        show pauling neutral at left with dissolve
        p "Here we are. Keep your phone close in case of emergencies. My dorm room is right next to yours. Come to the office at 6 ‘o clock."
        a "Roger that."
        p "Good night."
        a "Good night."
        hide pauling with moveoutleft
        "Pauling went to her own dorm. I changed into a purple pyjama that was folded on my bed."
        "I looked at myself up and down in the two-piece night-time clothing."
        "It’s funny how the pyjama matches my uniform. It’s not like anyone else but I’m going to see this. Why do pyjamas have to match the uniform?"
        "I shrug. Well why not? "
        scene black with dissolve
        "I shut the light and crawl under the blanket."
        "I lay awake for a while processing everything that’s happened today."

        if Demoman:
            "My kidnapping, the tank operator’s overenthusiastic greeting and his horrid file, magic being real and many hours of labour."
    
        else:
            "My kidnapping, the tank operator’s overenthusiastic greeting and his horrid file and many hours of labour."
            jump no_demoman2
    
    label no_demoman2:
        "My stomach grumbles. I remember I barely ate anything today."
        "Fortunately I was already tired so my thoughts and hunger didn’t keep me awake the rest of the night."
        "My alarm clock beeps. I hit its top and the godawful noise ceases."
        scene dorm with dissolve
        "I change into my work uniform. Soon I hear a knock on the door."
        a "Yes?"
        p "It’s me. Come out when you’re ready. I’ll explain the food related stuff next."
        "My eyes lit up. I’m full of energy. I’m so hungry I could eat both a horse and a cow. Dead or alive."
        "I come out of my dorm room. Despite the joy I feel on the inside, I keep my face serious and body language calm."
        "Great. I was wondering where and how we get food."
        "Miss Pauling smiled at me and asked me to follow her. She’s probably starving too."

        scene cafeteria with dissolve
        "She led me to a school cafeteria-looking room. She told me that the mercenaries eat breakfast in a room like this as well but they have their own. Pauling and I would come here when we’re hungry."
        "We just have to make it quick. We are busy women."

        scene office with dissolve
        "My typewriter makes a satisfying sound every time I press a button. I was a few hours in some work Miss Pauling has given me."
        "The room smelled like wooden furniture."
        "Some of the typewriter’s keys were more worn out than the others. Such as E, T, A and O."
        "An abrupt noise broke my concentration."
        "It was Miss Pauling’s phone."
        show pauling neutral
        p "Pauling here."
        p doubt "..."
        "She looked surprised. Did Admin give her a weird task?"
        p "Ahmavaara. This is for you."
        hide pauling
        "My brows flew up and my heart skipped a beat. What does Admin want from me? A task solely for me? On my second day?"
        show phone
        "I carefully pick the brick-looking phone from Pauling and put it to my ear."
        a "It’s Ahmavaara."
        show tank phone happy with dissolve
        t "Tereve!"
        "All of the tension leaves my body. In its place comes disappointment."
        a "You...? What do you need?"
        t phone neutral "I don’t need anything. I wanted to call you."
        a "Why?"
        t "To ask how you are."
        hide tank
        hide phone

        menu:
            "Don’t bother me.":
                jump dont_bother_me
            
            "I’m allright…":
                jump im_allright
            
            "I’m allright. How about you?":
                jump im_allright_how_about_you
        
        label dont_bother_me:
        show phone
        show tank phone embarrassed
        t "I don’t mean to bother you. I intent this to be quick."
        a "I said don’t bother me!"
        hide tank
        "I hang up on him."
        "Ugh! I hope he’s smart enough to not call again."
        jump after_tank_phone_call

        label im_allright:
        show phone
        show tank phone neutral
        "I sigh shaking my head."
        a "I’m allright…"
        t phone happy "How great!"
        "I sense him beaming."
        t phone neutral "Were you working before I called?"
        a "Obviously."
        show tank phone surprised with dissolve
        t "Oh! Sorry to interrupt something. I intend on making this quick."
        a "Mhm."
        t phone neutral "Second workday! Has it been tough?"
        "I shrug."
        a "The tasks aren’t hard. Just time-consuming."
        t "Is that good or bad? Would you rather them to be hard and quick?"
        "I shake my head and furrow my brows. What kinda question is that?"
        a "I have no preference…"
        a "Ugh. This conversation is dumb."
        t "I know, I know."
        "He wasn’t offended. Just amused."
        t phone sad "You probably find it hard as well to talk to strangers."
        a "I do."
        t "I apologize for asking dumb questions."
        t phone neutral "Anyway. I promised to keep my call short. See you! Hopefully in person if we’re in luck."
        a "If {i}you’re{/i} in luck."
        show tank phone happy
        "I corrected him. The tank operator chuckles."
        t "If I’m in luck. Now toodle-oo, Miss Ahmavaara!"
        a "Toodle-oo…"
        hide tank with dissolve
        "I repeat. That stupid word left a bad taste in my mouth. Tank hung up right after."
        jump after_tank_phone_call
        
        label im_allright_how_about_you:
        
        show phone
        show tank phone happy
        t "I’m doing alright too. Thanks for asking!"
        "I sense him beaming."
        t phone doubt "Well… I’d be doing even better if the rest of the fellas would stop pestering me about you…"
        "I glare at the floor."
        a "About me? Why?"
        t phone neutral "I don’t talk in crowds. Hell, I never even talk to three of the mercenaries I work with."
        show tank phone sad with dissolve
        "He sighed."
        t "Anyway. Uh. Now that I talked to you yesterday, everyone’s teasing me about you."
        show tank phone embarrassed with dissolve
        t "Don’t misunderstand! I didn’t call to complain. Everything’s fine."
        "He regains his composure."
        t phone neutral "You know how men are. They’ll stop when they realise they won’t get a reaction outta me and get bored."
        "He said that so I wouldn’t get worried. How dare he assume so of me?"
        a "That’s how it usually happens, yes. Or not."
        t phone sad "Yes. Sorry for dumping that information on you. You didn’t need to know that."
        a "No, I didn’t."
        t phone neutral "I promised to keep my call short. See you! Hopefully in person if we’re in luck."
        a "If {i}you’re{/i} in luck."
        show tank phone happy
        "I corrected him. The tank operator chuckles."
        t "If I’m in luck. Now toodle-oo, Miss Ahmavaara!"
        a "Toodle-oo…"
        hide tank with dissolve
        "I repeat. That stupid word left a bad taste in my mouth. Tank hung up right after."
        jump after_tank_phone_call

        label after_tank_phone_call:
        "I return Miss Pauling’s phone back to her."
        hide phone
        show pauling neutral
        p "Done? Good. Let’s get back to work."
        jump chapter4
    
label chapter4:
    scene black
    "Chapter 4"
    scene hallway
    "Miss Pauling and I carry our own tall stacks of papers and folders. We were a little tense from urgency. This task has a deadline. We usually walk slower."
    if Demoman:
        show demoman neutral at left 
        with seaseinleft
        "We come across a few mercenaries in the hallway. The magic man himself greets us when we scurry past him."
        hide demoman with easeoutleft
    
    else:
        show demoman neutral at left 
        with easeinleft
        "We come across a few mercenaries in the hallway. Demoman greets us when we scurry past him."
        hide demoman with easeoutleft
    
    show heavy neutral at right 
    with easeinright
    "Heavy sees us but decides not to react."
    hide heavy with easeoutright
    show scout happy with hpunch
    scout "Heyy! Miss Pauling!"
    show scout at right 
    with easeinleft
    show pauling sad at left
    with vpunch
    p "GAH!"
    show scout surprised
    "Scout ran from out of nowhere. Miss Pauling jumps and drops some of the papers on the ground. I tightened my grip on my papers so much my veins became visible." 
    "I wanted to show that pathetic excuse of a man how furious he’s made me but I kept my composure."
    p angry "Scout! Look what you’ve done!"
    hide pauling with easeoutbottom
    show scout sad
    "She squats down, placed the papers on the floor and started collecting what she dropped."
    "As much as I fully believe she’ll collect them in no time, I want to have a good relationship with her so I help her collect the papers. Scout does the same."
    hide scout with easeoutbottom
    show scout at right
    show pauling angry at left
    with dissolve
    show scout sad
    scout "Aw! Miss Pauling, I’m sorry. Didn’t mean to scare ya like that."
    "When the three of us have cleaned up, we stand up. Miss Pauling yanked the papers Scout collected from his hands."
    p "This better be the last time you’ll come up to me or Miss Ahmavaara like that. We have a deadline! You’ve wasted our really valuable time! I ought to shoot you next time."
    hide scout
    hide pauling
    with dissolve
    "We turn away but he stops us."
    show scout surprised at right with moveinright
    scout "Miss Pauling. I…"
    show pauling angry at left with moveinleft
    with hpunch
    p "What?!"
    show scout embarrassed
    scout "You… Uh…"
    scout "…Look very good today."
    p "Ugh!"
    hide scout
    hide pauling
    "She and I quickly pace away."
    scene office with dissolve

    show pauling angry with moveinright
    p "What is wrong with him?"
    hide pauling

    menu:
        "He definitely has a crush on you.":
            show pauling surprised
            p "What?"
            a "You haven’t noticed how he looks at you? And how he flirted at you back there?"
            p doubt "To be honest, I’ve never paid attention to him. I’ve been too busy."
            a "How do you feel about him having feelings for you?"
            p "I don’t think I… feel anything."
            p sad "Is that bad?"
            a "On his case no. I’ll tell you a little secret. I don’t like him."
            p happy "Is that so? I haven’t noticed that either."
            p neutral "Hmm. Now that I have 50 percent less work thanks to you, I could maybe pay a little more attention to my surroundings."
            p happy "Maybe I’ll notice who has a crush on you."
            "I crack a smile at her."
            a "Oh you."
            p surprised "Hey! The deadline! We mustn’t forget!"
            hide pauling with moveoutright
            "We quickly start working our typewriters as if this was the last day before the end of the world."

        "I know right. What an idiot.":
            show pauling sad
            p "Let’s just forget all about him. We need to get the work done."
            "I place the files next to my typewriter on my desk."
            a "I agree."
            hide pauling with moveoutright
            "We sit down and work our asses off."
    
    scene black with dissolve
    "We had to rush. Rush as accurately as we can because mistakes were out of the question. There had to be a balance. At the end of the day we finished the job."
    
    scene office with slideleft
    "When we came back from the cafeteria, we were already given another task. We were a couple of hours in."
    admin "Mission begins in ten seconds."
    "I raise my gaze from the file I’m working on. I recognise the admin’s voice. The announcement boomed from outside."
    admin "Five. Four. Three. Two. One."
    show pauling neutral
    p "What is it?"
    p surprised "Ooh! I just remembered this is your first time seeing RED and BLU fighting!"
    "She stands up."
    show office with dissolve:
        xzoom 1.3
        yzoom 1.3
    
    show pauling happy at left 
    p "Come to the window. We can see them going at it."
    hide pauling
    "I get up and look out the window with her. I see Soldier rocket jumping, Engineer building, a tank slowly approaching the enemy and Heavy opening fire. I could list dozens of things more that are happening right now."
    "One of the men just exploded into bits. Body parts and blood gets everywhere. Somebody stops to laugh at that."
    show pauling neutral at left
    p "Hypothetical question."
    p "Would you rather be working here, have almost no free time but you’d be safe and warm inside this building or work there? You’d have a bunch of free time but you could get wounded any second."
    hide pauling

    default here = False

    menu:
        "Here.":
            $ here = True
            a "I’d have to move all the time and be outdoorsy if I worked there."
            show pauling neutral at left 
            p "Agreed."

        "There.":
            a "Killing people is part of my contract already. Why not get rid of the paperwork aspect?"
            show pauling neutral at left 
            p "You do have a point."

    p "I’d definitely have this job rather than a mercenary’s. I like the safe and warm part."
    p happy "I know I won’t be safe and warm at all times but still."
    p neutral "Working here is nice and quiet."

    if here:
        a "I agree with you 100 percent."
        show pauling happy at left
        "She smiles at me and gets back to work."
    
    a "I agree."
    show pauling neutral at left
    "She smiles at me and gets back to work."

label chapter5:
    scene black
    "Chapter 5"
    scene hallway with dissolve






    
    
    return