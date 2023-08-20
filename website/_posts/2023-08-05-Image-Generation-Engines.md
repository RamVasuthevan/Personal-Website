---
layout: post
title:  "The World Has Changed"
permalink: bitsbipsbricks/Image-Generation-Engines
---

**Editor's Note: This was written in September 2022. At the time, I wanted to add more about what I thought image generators would be used for, and then I procrastinated ... a lot. But I've decided to publish this version for posterity. The world has changed, and still almost nobody knows it yet.**

Today is September 6th, 2022. The three main image generation engines are DALL-E 2, Stable Diffusion, and Midjourney. (The date is important. The leading engines could be different a week from now.) Two months ago, the creation of digital artwork cost $100's dollars or $1000's dollars an image and photography costs $10's and $1000's per image. Today, the creation of digital images costs cents. Images can now be generated in seconds, by giving an image generation engine a text prompt and by fiddling with two or three simple parameters.

DALL-E 2 was released on July 20th, 2022. OpenAI, one of the world's leading research laboratories, created it. OpenAI has XX[^1] employees. It was closed-sourced and available initially only to beta testers on the waitlist. OpenAI distorted any faces in images making it hard to be used for deep fakes. Stability AI released Stable Diffusion on August 22nd, 2022, 33 days later. Stable Diffusion is open source, can be run on a consumer GPU, and doesn't blur faces like DALL-E 2. Stability AI, as of August 12th, 2022, has 75 employees.


{% include image.html 
   src="/assets/bitsbipsbricks/Image-Generation-Engines/out-1.png" 
   alt="" 
   caption="Created by Stable Diffusion using [Replicate](https://replicate.com/p/xipb7ajpnretfmu42z3yxnhwuu)" 
%}



The images aren’t prefect. They still gave off a weird vibe. And giving the right words to get the image you want (prompt engineering[^2]) is still a bit finicky. But an hour after I started playing with Stable Diffusion, I was able to create this image of an Canadian Flag and an Astronaut on the moon. (So can you with [Stable Diffusion](https://replicate.com/p/xipb7ajpnretfmu42z3yxnhwuu) on commit `a9758cbfbd5f` with width `512` height `512` prompt `Neil Armstrong on the Moon Canadian Flag` num_outputs `4` guidance_scale `7` prompt_strength `0.8` num_inference_steps `129` and seed `47692`).

More:
- Soon for videos, etc
- Fundamentally, a different medium
- Deepfakes
- Creative labour
- New art created (Comic book etc)
- Programmatic creation (See what clothes would look like on you?, What products look like your home?)
- Meaning of non-human-created artwork?
- Creative work of curation??
- Can't be put back in the box. This felt different. We were/aren't ready.
- **We won't be ready for the next one**

[^1]: I didn't find the number at the time and couldn't find the exact number now
[^2]: I've changed my mind about what prompt engineering is. Prompt Engineering vs. Blind Prompting — Mitchell Hashimoto