# Reinforcement-Learning-Atari-Game-

## Idea 
In the world of ML, a technique called Transfer Learning is often used to save time, computing power, and yields accurate predictions. The idea is to apply transfer learning into reinforcement learning, in this case Atari games. 

I wanted to assess the abstraction capabilities of RL algorithms by training an agent on a single environment, and subsequently transferring the learned ‘weights’ to another similar environment. For the expirement, i picked two games available in the OpenAI gym, Space Invaders and Demon Attack. 

I leveraged DQN Architecture to train the first agent on the “Space Invader" and then applied the weights onto Demon Attack. 

#### DQN Archit 
<img src="https://github.com/UWMonkey/Reinforcement-Learning-Atari-Game-/blob/master/images/DQN.png" height="400" width="800">

DQN leverages convolutional neural network, and inorder to speed up the training that is compatible with my computer, i decided to rescale each frame to 84*84 and grey-scale. While only maintaining 4 consecutive frames as learning images. 

#### Training Setup
<img src="https://github.com/UWMonkey/Reinforcement-Learning-Atari-Game-/blob/master/images/setup.PNG" height="400" width="800">

Now is time to train the agent, for the DQN training i trained with, Greedy Policy (ξ = 0.1), Discount Factor (γ = 0.99), 10 Episode of random game play

#### Game play

Pre-trained | Trained
------------ | -------------
<img src="https://github.com/UWMonkey/Reinforcement-Learning-Atari-Game-/blob/master/images/space_random_cut.gif" height="250" width="250">|<img src="https://github.com/UWMonkey/Reinforcement-Learning-Atari-Game-/blob/master/images/spaceinvader_trained_final_cut.gif" height="250" width="250">

OK! after 5100 episodes the agent learns how to play Space Invader fairly well. So, the highest score achieved was 600, guess it needed more time to train inorder to beat me.

#### Agent Rewards for 5100 ep | Average Max-Q for 5100 ep

<img src="https://github.com/UWMonkey/Reinforcement-Learning-Atari-Game-/blob/master/images/space_agent_reward.png" height="350" width="450">| 
<img src="https://github.com/UWMonkey/Reinforcement-Learning-Atari-Game-/blob/master/images/space_agent_score.png" height="350" width="450">

#### Its time to apply Space Invader agent to Demon Attack!
Without any training, lets observed the pre-trained model (applying space invader weights directly） and a new agent just start playing Demon Attack

Pre-trained | Random Agent
------------ | -------------
<img src="https://github.com/UWMonkey/Reinforcement-Learning-Atari-Game-/blob/master/images/Space_to_demon_random_cut.gif" height="250" width="250">|<img src="https://github.com/UWMonkey/Reinforcement-Learning-Atari-Game-/blob/master/images/Demon_random_cut.gif" height="250" width="250">

I think something is off， new agent is playing better than my pre-trained agent from space-invader. Maybe a little training might help on the model. So i decided to train both model, transfered agent and a new agent just over 300 eps for fair comparsion. 

Space-invader Agent Trained | Demon Attack Agent
------------ | -------------
<img src="https://github.com/UWMonkey/Reinforcement-Learning-Atari-Game-/blob/master/images/Space_to_demon_trained_cut.gif" height="250" width="250">|<img src="https://github.com/UWMonkey/Reinforcement-Learning-Atari-Game-/blob/master/images/Demon_trained_300epi_cut.gif" height="250" width="250">

#### Max-Q for the training

Space-invader Agent Trained | Demon Attack Agent
------------ | -------------
<img src="https://github.com/UWMonkey/Reinforcement-Learning-Atari-Game-/blob/master/images/space_demon_reward.png" height="350" width="450">|<img src="https://github.com/UWMonkey/Reinforcement-Learning-Atari-Game-/blob/master/images/demon_new_300.png" height="350" width="450">

#### Result Comparsion for Greedy Policy (ξ = 0.1), Discount Factor (γ = 0.99) best of 30 eps :

Space-invader Agent Trained | Demon Attack Agent
------------ | -------------
average reward = 16 | average reward =21
average Max-Q = 2.2 | average Max-Q = 0.72
Highest Game Score = 460 | Highest Game Score = 860

So, something interesting occured, the transfered agent did have a head start on learning, however it was stuck in a loophole and did not improve much. Whereas, the blank new agent, started-off slow but picked up later. So i started to examine maybe was the game design that the space invader agent picked up. Then i realized that it picked up a bad habbit in space-invader game and trying to apply to demon attack. 

Space-invader | Demon Attack Agent
------------ | -------------
<img src="https://github.com/UWMonkey/Reinforcement-Learning-Atari-Game-/blob/master/images/space_safe.PNG" height="350" width="450">|<img src="https://github.com/UWMonkey/Reinforcement-Learning-Atari-Game-/blob/master/images/demon_not_safe.PNG" height="350" width="450">

So i notice that space-invader has these safe zones where it can hide the ship and not die. It tried to apply the same concept into demon attack, but it is not so safe in demon attack again. Thats why the pre-trained agent was constantly going to the side.

### Key Learnings 

A DQN algorithm trained on Space Invaders was unable to reproduce success on Demon Attack. This can be attributed to the fact that while the action sets for the two games are identical, the respective environments are distinct. Transfer-learning can be helpful to give a head start, however it is likely to also carry bad habits. Well that was fun :)




