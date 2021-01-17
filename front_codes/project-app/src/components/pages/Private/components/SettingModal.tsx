import React, { FC } from 'react'
import { Modal } from '@material-ui/core'

interface SettingModalProps {
  onModal: boolean;
  setOnModal : any;
}

const SettingModal: FC<SettingModalProps> = ({ onModal, setOnModal }) => {
  return (
    <Modal
      open={onModal}
      onClose={() => setOnModal(false)}
      aria-labelledby="Settings"
      aria-describedby="simple-modal-description"
    >
      <div>Settings Contents</div>
    </Modal>
  )
}

export default SettingModal
