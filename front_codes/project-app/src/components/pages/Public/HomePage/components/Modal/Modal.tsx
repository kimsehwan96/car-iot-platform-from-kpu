import React, { FC, useCallback, useEffect, useRef } from 'react';
import { useSpring, animated } from 'react-spring';
import { Background, CloseModalButton, ModalContent, ModalImg, ModalWrapper } from './modalElements'

interface ModalProps {
  textInModal: any;
  showModal: boolean;
  setShowModal: any
}

const Modal: FC<ModalProps> = ({ showModal, setShowModal, textInModal }) => {
  const modalRef = useRef();

  const animation = useSpring({
    config: {
      duration: 250
    },
    opacity: showModal ? 1 : 0,
  });

  const closeModal = (e: any)=> {
    if (modalRef.current === e.target) {
      setShowModal(false);
    }
  }

  const keyPress = useCallback(
    (e: any) => {
      if(e.key === 'Escape' && showModal) {
      setShowModal(false);
      }
    }, 
    [setShowModal, showModal]
  );

  useEffect(
    () => {
      document.addEventListener('keydown', keyPress);
      return () => document.removeEventListener('keydown', keyPress);
    },
    [keyPress]
  );

  return (
    <>
    {showModal ? 
      <Background ref={modalRef} onClick={closeModal}>
        <animated.div style={animation}>
          <ModalWrapper showModal={showModal}>
            <ModalImg alt="Input the Img" />
            <ModalContent>
              {textInModal}
            </ModalContent>
            <CloseModalButton 
              aria-label='Close modal'
              onClick={() => setShowModal((prev: boolean) => !prev)}
            />
          </ModalWrapper>
        </animated.div> 
      </Background>    
    : null}
    </>
  )
}

export default Modal
