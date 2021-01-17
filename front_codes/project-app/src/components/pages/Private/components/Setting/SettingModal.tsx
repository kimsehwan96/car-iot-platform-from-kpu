import React, { FC, useState } from 'react'
import { Modal } from '@material-ui/core'
import { getModalStyle, useStyles } from './styles'

interface SettingModalProps {
  onModal: boolean;
  setOnModal : any;
}

const SettingModal: FC<SettingModalProps> = ({ onModal, setOnModal }) => {
  const classes = useStyles();
  const [modalStyle] = useState(getModalStyle);

  return (
    <Modal
      open={onModal}
      onClose={() => setOnModal(false)}
      aria-labelledby="Settings"
      aria-describedby="simple-modal-description"
    >
      <div style={modalStyle} className={classes.paper}>
        Settings Contents
      </div>
    </Modal>
  )
}

export default SettingModal
