import React, { FC } from 'react'
import { animateScroll as scroll } from 'react-scroll'
import { FaFacebook, FaInstagram, FaYoutube } from 'react-icons/fa';
import { FooterContainer, FooterLink, FooterLinkItems, FooterLinksContainer, FooterLinksWrap, FooterLinkTitle, FooterWrap, SocialIconLink, SocialIcons, SocialLogo, SocialMedia, SocialMediaWrap, WebsiteRights } from './footerElements';

const Footer: FC = () => {

  const toggleHome = () => {
    scroll.scrollToTop();
  }
  return (
    <FooterContainer>
      <FooterWrap>
        <FooterLinksContainer>
          <FooterLinksWrap>
            <FooterLinkItems>
              <FooterLinkTitle>About us</FooterLinkTitle>
                <FooterLink to="#">How it works</FooterLink>
                <FooterLink to="#">Our Team</FooterLink>
                <FooterLink to="#">Teams of Service</FooterLink>
            </FooterLinkItems>
            <FooterLinkItems>
              <FooterLinkTitle>Contact us</FooterLinkTitle>
                <FooterLink to="#">Contact</FooterLink>
                <FooterLink to="#">Support</FooterLink>
                <FooterLink to="#">Sponsorships</FooterLink>
            </FooterLinkItems>
            <FooterLinkItems>
              <FooterLinkTitle>Videos</FooterLinkTitle>
                <FooterLink to="#">Submit Video</FooterLink>
                <FooterLink to="#">Agency</FooterLink>
                <FooterLink to="#">Ambassadors</FooterLink>
            </FooterLinkItems>
            <FooterLinkItems>
              <FooterLinkTitle>Social Media</FooterLinkTitle>
                <FooterLink to="#">Instagram</FooterLink>
                <FooterLink to="#">Facebook</FooterLink>
                <FooterLink to="#">Youtube</FooterLink>
            </FooterLinkItems>
          </FooterLinksWrap>
        </FooterLinksContainer>
        <SocialMedia>
          <SocialMediaWrap>
            <SocialLogo to='/' onClick={toggleHome}>
              Logo
            </SocialLogo>
            <WebsiteRights>
              kwhong ©{new Date().getFullYear()} All rights reseved.
            </WebsiteRights>
            <SocialIcons>
              <SocialIconLink href="/" target="_blank" aria-label="Facebook"><FaFacebook /></SocialIconLink>
              <SocialIconLink href="/" target="_blank" aria-label="Instagram"><FaInstagram /></SocialIconLink>
              <SocialIconLink href="/" target="_blank" aria-label="Youtube"><FaYoutube /></SocialIconLink>
            </SocialIcons>
          </SocialMediaWrap>
        </SocialMedia>
      </FooterWrap>
    </FooterContainer>
  )
}

export default Footer;
