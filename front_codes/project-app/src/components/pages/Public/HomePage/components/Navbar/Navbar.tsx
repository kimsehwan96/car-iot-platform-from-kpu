import React, { FC, useEffect, useState } from 'react'
import { FaBars } from 'react-icons/fa';
import { IconContext } from 'react-icons/lib';
import { MobileIcon, Nav, NavbarContainer, NavItem, NavLogo, NavMenu, NavLinks, NavBtn, NavBtnLink } from './navebarElements';
import { animateScroll as scroll } from 'react-scroll';

interface NavbarProps {
  toggle: () => void;
}


const Navbar: FC<NavbarProps> = ({ toggle }) => {
  const [scrollNav, setScrollNav] = useState(false);

  const changeNav = () => {
    if(window.scrollY >= 80 ) {
      setScrollNav(true);
    } else {
      setScrollNav(false);
    }
  }

  useEffect(() => {
    window.addEventListener('scroll', changeNav);
  }, []);

  const toggleHome = () => {
    scroll.scrollToTop();
  }

  return (
    <>
      <IconContext.Provider value={{ color: '#fff' }}>
        <Nav scrollNav={scrollNav}>
          <NavbarContainer>
            <NavLogo to="/" onClick={toggleHome}>Logo</NavLogo>
          <MobileIcon onClick={toggle}>
            <FaBars />
          </MobileIcon>
          <NavMenu>
            <NavItem>
              <NavLinks 
                to='dashboard'
                smooth={true}
                duration={500}
                spy={true}
                activeClass='active'
                offset={-80}
              >
                Dashboard
              </NavLinks>
            </NavItem>
            <NavItem>
              <NavLinks 
                to='analysis'
                smooth={true}
                duration={500}
                spy={true}
                activeClass='active'
                offset={-80}
              >Analysis
            </NavLinks>
            </NavItem>
            <NavItem>
              <NavLinks 
                to='expectations'
                smooth={true}
                duration={500}
                spy={true}
                activeClass='active'
                offset={-80}
              >
                Expectations
              </NavLinks>
            </NavItem>
            <NavItem>
              <NavLinks 
                to='signup'
                smooth={true}
                duration={500}
                spy={true}
                activeClass='active'
                offset={-80}
              >
                Sign Up
              </NavLinks>
            </NavItem>
          </NavMenu>
            <NavBtn>
              <NavBtnLink to='/signin'>Sign In</NavBtnLink>
            </NavBtn>
          </NavbarContainer>
        </Nav> 
      </IconContext.Provider>
    </>
  )
}

export default Navbar;
