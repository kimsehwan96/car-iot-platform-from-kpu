import React from 'react'
import { 
    DashboardFilled,
    PieChartFilled,
    WechatFilled,
    SoundFilled,
} from '@ant-design/icons';

export const SidebarData = [
    {
        id: 1,
        title: 'Dashboard',
        path: '/dashboard',
        icon: <DashboardFilled />,
        cName: 'nav-text',
        desc: '차량 체크 요소를 한눈에 파악하자',
    },
    {
        id: 2,
        title: 'Pattern',
        path: '/pattern',
        icon: <PieChartFilled />,
        cName: 'nav-text',
        desc: '나의 운전 실력을 분석해보자',
    },
    {
        id: 3,
        title: 'Community',
        path: '/community',
        icon: <WechatFilled />,
        cName: 'nav-text',
        desc: '운전 분석 결과를 사람들과 공유하자'
    },
    {
        id: 4,
        title: 'ContactUs',
        path: '/contactus',
        icon: <SoundFilled />,
        cName: 'nav-text',
        desc: '개선점 및 불편사항을 알려주세요'
    },
]