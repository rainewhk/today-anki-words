import json
import os
from datetime import datetime, timedelta, timezone

from fastanki import *

# from dotenv import load_dotenv
# load_dotenv()

sync(
    user=os.getenv("ANKI_USER"), passw=os.getenv("ANKI_PASS"), upload=False, media=False
)

col = Collection.open()

# cards = find_cards("prop:due=0")

cards = col.find_cards(deck="单词记忆背诵", is_due=True)

print(len(cards))

note_ids = {card.nid for card in cards}
notes = {col.get_note(note_id) for note_id in note_ids}
fields = [note.fields for note in notes]

tz_utc_plus_8 = timezone(timedelta(hours=8))
current_date = datetime.now(tz_utc_plus_8).strftime("%Y%m%d")

with open(f"data/{current_date}.json", "w", encoding="utf-8") as f:
    json.dump(fields, f, indent=4, ensure_ascii=False)
