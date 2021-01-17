import React, { FC, useState } from 'react'
import { Modal, Switch, Typography } from '@material-ui/core'
import { getModalStyle, useStyles } from './styles'

interface SettingModalProps {
  onModal: boolean;
  setOnModal : any;
  darkMode : any;
  setDarkMode : any;
}

const SettingModal: FC<SettingModalProps> = ({ onModal, setOnModal, darkMode , setDarkMode }) => {
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
        <Typography variant="h4">Settings</Typography>
        <Typography>Dark Mode?</Typography>
        <Switch checked={darkMode} onChange={() => setDarkMode(!darkMode)} />
      </div>
    </Modal>
  )
}

export default SettingModal
