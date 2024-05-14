import { height } from '@mui/system';
import React from 'react';
import DangerousIcon from '@mui/icons-material/Dangerous';
import Poison from '../assets/poison.png'

export default function Server({ isPoisoned, SpamPer }) {
  return (
    <div className='server_container'>
        {isPoisoned && (
            <div className='poison_img_container'>
                <img src={Poison} className="poison_img" alt="poisoned" />
            </div>
        )}
        <div className={`server ${SpamPer>=50 ? 'server_invalid' : 'server_valid'}`}>
            <div className='server_class server_ham_class' style={{width:`${100 - SpamPer}%`}}>
                Ham <br/> {100 - SpamPer}%
            </div>
            <div className='server_class server_spam_class' style={{width:`${SpamPer}%`}}>
                Spam <br/> {SpamPer}%
            </div>
        </div>
    </div>

  );
}
