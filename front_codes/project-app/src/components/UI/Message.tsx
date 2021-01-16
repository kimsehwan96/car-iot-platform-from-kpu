import React, { FC } from 'react';

interface MessageProps  {
  msg: string;
  type: 'danger' | 'success';
}

const Message: FC<MessageProps> = ({ msg, type }) => {
  let typeClass = '';

  if (type === 'danger') {
    typeClass = 'is-danger';
  }

  if (type === 'success') {
    typeClass = 'is-success'
  }

  return (
    <article className={`message ${typeClass}`}>
      <div className="message-body">{msg}</div>
    </article>
  )
}

export default Message;
