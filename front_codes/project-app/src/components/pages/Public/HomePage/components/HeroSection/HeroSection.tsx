import React, { FC, useState } from 'react';
import HomeVidio from '../../../asserts/HomeVidio.mp4';
import { motion } from 'framer-motion';
import { Button } from '../buttonElements';
import { ArrowForward, ArrowRight, HeroBg, HeroBtnWrapper, HeroContainer, HeroContent, HeroH1, HeroP, VideoBg } from './heroElements';

const HeroSection: FC = () => {
  const [hover, setHover] = useState(false);

  const onHover = () => {
    setHover(!hover);
  }

    const fadeLeft = {
      hidden: { opacity: 0, x: -100 },
      visible: { opacity: 1, x: 0 }
    }

  return (
    <HeroContainer>
      <HeroBg>
        <VideoBg autoPlay loop muted src={HomeVidio} typeof="video/mp4" />
      </HeroBg>   
      <HeroContent>
      <HeroH1>
        <motion.h1
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 1 }}
        >
          Driving Mate  
        </motion.h1>
      </HeroH1>
      <HeroP>
        <motion.p
          variants={fadeLeft}
          initial='hidden'
          animate='visible'
          transition={{ duration: 1 }}
        >
          Good friend of your car!
          I'll show you everything you're curious about.
        </motion.p>
      </HeroP>
      <HeroBtnWrapper>
        <Button 
          to='dashboard' 
          onMouseEnter={onHover} 
          onMouseLeave={onHover}
          primary='true'
          dark='true'
          smooth={true}
          duration={500}
          spy={true}
          offset={-80}
        >
          Get started {hover ? <ArrowForward /> : <ArrowRight/> }
        </Button>
      </HeroBtnWrapper>
    </HeroContent>
    </HeroContainer>
  )
}

export default HeroSection
