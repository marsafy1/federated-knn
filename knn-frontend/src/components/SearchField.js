import * as React from 'react';
import Paper from '@mui/material/Paper';
import InputBase from '@mui/material/InputBase';
import Divider from '@mui/material/Divider';
import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';
import SearchIcon from '@mui/icons-material/Search';
import DirectionsIcon from '@mui/icons-material/Directions';
import BedtimeIcon from '@mui/icons-material/Bedtime';
import CatchingPokemonIcon from '@mui/icons-material/CatchingPokemon';
import ChevronRightIcon from '@mui/icons-material/ChevronRight';
import CasinoIcon from '@mui/icons-material/Casino';
import ShuffleIcon from '@mui/icons-material/Shuffle';
import Tooltip from '@mui/material/Tooltip';

export default function SearchField() {
  return (
    <Paper
      component="form"
      sx={{ p: '2px 4px', display: 'flex', alignItems: 'center', width: '100%', backgroundColor: 'var(--secondary-bg)', border: '1px solid var(--primary)' }}
    >
      <IconButton sx={{ p: '10px', color:'var(--primary)'}} aria-label="menu">
        <ChevronRightIcon />
      </IconButton>
      <InputBase
        sx={{ ml: 1, flex: 1 , color:'white'}}
        placeholder="Enter a Text to Classify"
        inputProps={{ 'aria-label': 'search google maps' }}
      />
      <Tooltip title="Generate Random Input">
        <IconButton type="button" sx={{ p: '10px', color:'var(--primary)'}} aria-label="search">
          <ShuffleIcon />
        </IconButton>
      </Tooltip>
      <Divider sx={{ height: 28, m: 0.5, background:'var(--primary)'}} orientation="vertical" />
      <Tooltip title="Classify Input">
        <IconButton  sx={{ p: '10px', color:'var(--primary)' }} aria-label="directions">
          <SearchIcon />
        </IconButton>
      </Tooltip>
    </Paper>
  );
}
