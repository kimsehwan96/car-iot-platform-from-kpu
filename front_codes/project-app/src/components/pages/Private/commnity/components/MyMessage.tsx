import React, { FC } from 'react';

interface MyMessageProps {
  message: any;
}

const MyMessage: FC<MyMessageProps> = ({ message }) => {
  if ( message?.attachments?.length > 0 ) {
    return (
      <img 
        alt="message-attachment"
        src={message.attachments[0].file}
        className="message-image"
        style={{ float: 'right' }}
      />
    )
  }

  return (
    <div className="message" style={{ float: 'right', marginRight: '18px', color: 'white', backgroundColor: "#333" }}>
      {message.text}
    </div>
  )
}

export default MyMessage;
