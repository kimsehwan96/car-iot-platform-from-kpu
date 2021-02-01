import React, { FC } from 'react';

import MyMessage from './MyMessage';
import OtherMessage from './OtherMessage';
import MessageForm from './MessageForm';

interface Props {
  chats: any;
  activeChat: any;
  userName: string;
  message: string;
}

const ChatFeed: FC= ( props: Props | any ) => {
  const { chats, activeChat, userName, messages } = props;

  const chat = chats && chats[activeChat];

  const renderMessage = () => {
    const keys = Object.keys(messages);

    return keys.map(( key, index ) => {
      const message = messages[key]
      const lastMessageKey = index === 0 ? 'null' : keys[index - 1];
      const isMyMessage = userName === message.sender.username; 

      console.log(message);
      return (
        <div key={`msg_${index}`} style={{ width: '100%' }}>
          <div className="message-block">
            {
              isMyMessage ? <MyMessage message={message} /> : <OtherMessage message={message} lastMessage={message[lastMessageKey]} />
            }
          </div>
          <div className="read-receipts" style={{ marginRight: isMyMessage ? '16px' : '0px', marginLeft: isMyMessage ? '0px' : '68px' }}>
            read-receipts
          </div>
        </div>
      );
    })
  }

  return (
    <div className="chat-feed">
      <div className="chat-title-container">
        <div className="chat-title">{chat?.title}</div>
        <div className="chat-subtitle">
          {chat?.people.map((person: any) => `${person.person.username}`)}
        </div>  
      </div>
      {renderMessage()}
      <div style={{ height: '100px' }}>
        <div className="message-form-container">
          <MessageForm {...props} chat />
        </div>
      </div>
    </div>
  )
}

export default ChatFeed;
