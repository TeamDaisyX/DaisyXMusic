# Calls Music — The first open-source PyTgCalls based project

## Requirements

- FFmpeg
- NodeJS 15+
- Python 3.7+

## Deployment

### Config

Copy `example.env` to `.env` and fill it with your credentials.

### Without Docker

1. Install Python requirements:
   ```bash
   pip install -U -r requirements.txt
   ```
2. Run:
   ```bash
   python main.py
   ```

### Using Docker

1. Build:
   ```bash
   docker build -t musicplayer .
   ```
2. Run:
   ```bash
   docker run --env-file .env musicplayer
   ```

### Heroku

[Click here](https://github.com/callsmusic/callsmusicheroku)


## Credits

- [Roj](https://github.com/rojserbest) & [Marvin](https://github.com/BlackStoneReborn): development
- [Laky](https://github.com/Laky-64) & [Andrew](https://github.com/AndrewLaneX): PyTgCalls

## License

### GNU General Public License v3.0
[Read more](http://www.gnu.org/licenses/#GPL)
