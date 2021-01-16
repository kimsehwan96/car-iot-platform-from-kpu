import React, { FC } from 'react'
import { CloseIcon, Icon, SidebarBtnWrap, SidebarContainer, SidebarLink, SidebarMenu, SidebarRoute, SidebarWrapper } from './sidebarElements'

interface SidebarProps {
  isOpen: any;
  toggle: () => void;
}
// @ts-ignore
const Sidebar: FC<SidebarProps> = ({ isOpen, toggle }) => {
  return (
    <>
     <SidebarContainer isOpen={isOpen} onClick={toggle}>
       <Icon onClick={toggle}>
         <CloseIcon />
       </Icon>
       <SidebarWrapper>
        <SidebarMenu>
          <SidebarLink to="dashboard" onClick={toggle}>
            Dashboard
          </SidebarLink>
          <SidebarLink to="analysis" onClick={toggle}>
            Analysis
          </SidebarLink>
          <SidebarLink to="expectations" onClick={toggle}>
            Expectations
          </SidebarLink>
          <SidebarLink to="signup" onClick={toggle}>
            Sign Up
          </SidebarLink>
        </SidebarMenu>
        <SidebarBtnWrap>
          <SidebarRoute to='/signin'>Sign In</SidebarRoute>
        </SidebarBtnWrap>
       </SidebarWrapper>
     </SidebarContainer>
    </>
  )
}

export default Sidebar;
