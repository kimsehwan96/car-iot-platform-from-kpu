import React, { FC } from 'react';
import { ChatEngine } from 'react-chat-engine';

import './Chat.css';
import ChatFeed from './components/ChatFeed';

const Chat: FC = () => {
  return (
    <div className="root">
      <ChatEngine
        height = "100vh"
        projectID="eac34fe6-4fae-4713-a1b0-48378056c8f6" 
        userName="kwhong95"
        userSecret="123123"
        renderChatFeed = {(props: object) => <ChatFeed { ...props} /> }
      />
    </div>
  )
}

export default Chat;
