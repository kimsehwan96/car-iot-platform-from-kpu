import React, { FC } from 'react';

interface OtherMessageProps {
  message: any;
  lastMessage: any;
}

const OtherMessage: FC<OtherMessageProps> = ({ message, lastMessage }) => {
  const isFirstMessageByUser = !lastMessage || lastMessage.sender.username !== message.sender.username

  return (
    <div className="message-row">
      {isFirstMessageByUser && (
        <div 
          className="message-avatar"
          style={{ backgroundImage: `url(${message?.sender?.avatar})` }}
        />
      )}
      {message?.attachment?.length > 0
        ? (
          <img
            src={message.attachment[0].file}
            alt="message-attachment"
            className="message-img"
            style={{ marginLeft: isFirstMessageByUser ? '4px' : '48px' }}
          />
        ) : (
          <div className="message" style={{ float: 'left', backgroundColor: "#CABCDC", marginLeft: isFirstMessageByUser ? '4px' : '48px'  }}>
            {message.text}
          </div>
        )
      }
    </div>
  )
}

export default OtherMessage;
