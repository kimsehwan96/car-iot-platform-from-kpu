import React, { FC, useState } from 'react'
import Expectations from './components/Expectations/Expectations';
import Footer from './components/Footer/Footer';
import HeroSection from './components/HeroSection/HeroSection';
import { homeObjOne, homeObjTwo, homeObjThree } from './components/InfoSection/Data';
import InfoSection from './components/InfoSection/InfoSection';
import Navbar from './components/Navbar/Navbar'
import Sidebar from './components/Sidebar/Sidebar';

const HomePage: FC = () => {
  const [isOpen, setIsOpen] = useState(false);

  const toggle = () => {
    setIsOpen(!isOpen);
  }

  return (
    <>
      <Sidebar isOpen={isOpen} toggle={toggle} />
      <Navbar toggle={toggle} />
      <HeroSection />
      <InfoSection {...homeObjOne}/>
      <InfoSection {...homeObjTwo}/>
      <Expectations />
      <InfoSection {...homeObjThree}/>
      <Footer />
    </>
  )
}

export default HomePage;
