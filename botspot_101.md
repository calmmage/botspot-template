# Botspot 101: Core Components

`@botspot_command` only adds the command to the menu — still register the aiogram handler.

## Message & Command Components

### send_safe.py
```python
from botspot.utils.send_safe import send_safe

await send_safe(chat_id, "Very long message..." * 100)
```

### commands_menu.py
```python
from botspot.commands_menu import botspot_command, add_hidden_command, Visibility
from aiogram.filters import Command

@botspot_command("start", "Start the bot", visibility=Visibility.PUBLIC)
@router.message(Command("start"))
async def cmd_start(message): ...

@botspot_command("stats", "Show stats", visibility=Visibility.HIDDEN)
@router.message(Command("stats"))
async def cmd_stats(message): ...

@add_hidden_command("debug", "Debug info")
async def cmd_debug(message): ...
```

### i18n
```python
from botspot.i18n import t, register_strings

register_strings({"hello": {"en": "Hi {name}", "ru": "Привет {name}"}})
await send_safe(chat_id, t("hello", name="Ada"))
```

## Chat Management

### chat_fetcher.py
```python
from botspot import get_chat_fetcher

fetcher = get_chat_fetcher()
history = await fetcher.get_chat_messages(chat_id, user_id, limit=20)
```

### chat_binder.py
```python
from botspot.chat_binder import bind_chat, get_bound_chat, list_user_bindings

await bind_chat(user_id, chat_id)
bound_chat_id = await get_bound_chat(user_id)
bindings = await list_user_bindings(user_id)
```

## LLM Components

### llm_provider.py
```python
from botspot.llm_provider import aquery_llm_text, aquery_llm_structured, astream_llm

response = await aquery_llm_text(prompt="Summarize this article", user=user_id)

async for chunk in astream_llm(prompt="Write a story", user=user_id):
    collected_text += chunk

class Analysis(BaseModel):
    sentiment: str
    key_points: list[str]

result = await aquery_llm_structured(prompt="Analyze this", output_schema=Analysis, user=user_id)
```

## Interactive Components

### user_interactions.py
```python
from botspot.components.features.user_interactions import ask_user, ask_user_choice, ask_user_confirmation

response = await ask_user(chat_id=chat_id, question="What to search?", state=state)
choice = await ask_user_choice(chat_id=chat_id, choices=["News", "Sports"], state=state)
confirmed = await ask_user_confirmation(chat_id=chat_id, question="Proceed?", state=state)
choice = await ask_user_choice(chat_id=chat_id, choices={"1": "News", "2": "Sports"}, state=state)
if choice == "1":
    ...
```

## Data & Access Control

### postgres_database.py (preferred for new bots)
```python
from botspot.components.data.postgres_database import Base, get_session
from sqlalchemy.orm import Mapped, mapped_column

class Item(Base):
    __tablename__ = "items"
    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]

async with get_session() as session:
    session.add(Item(text="hi"))
    await session.commit()
```

Alembic lives in the app: `target_metadata = Base.metadata` after importing app models.

### mongo_database.py
```python
from botspot.components.data.mongo_database import get_database

db = get_database()
await db.users.update_one({"user_id": user_id}, {"$set": data}, upsert=True)
user = await db.users.find_one({"user_id": user_id})
```

### friends / admins
```python
from botspot.utils import is_admin, is_friend

if is_friend(user) or is_admin(user):
    ...
```

Env: `BOTSPOT_ADMINS_STR`, `BOTSPOT_FRIENDS_STR`. Persistent lists: `BOTSPOT_ACCESS_CONTROL_ENABLED=true` (needs Mongo).

### subscription_manager
```python
from botspot.subscription_manager import require_plan, get_subscription_manager

@require_plan()  # any paid entitlement; friends/admins bypass
@router.message(Command("premium"))
async def premium(message): ...

ent = await get_subscription_manager().check_entitlement(user_id)
```

Needs Mongo plus `BOTSPOT_SUBSCRIPTION_MANAGER_ENABLED=true`. This template keeps a commented `/premium` example in `src/router.py`.

### single_user_mode.py
```python
from botspot import is_single_user_mode_enabled, get_single_user

if is_single_user_mode_enabled():
    single_user = get_single_user()
```

## Using Components in Single User Mode

Single user mode drops `user_id` from most component calls:

- **LLM Queries**: `aquery_llm_text()` without `user`
- **Queue Management**: enqueue/dequeue without tracking `user_id`
- **Chat Binding**: bound chats without `user_id`
- **Database Operations**: user-specific data without extra filters
- **Telethon Operations**: the user's Telegram account

## Error Handling

```python
from botspot.core.errors import BotspotError

# Never use try/except — let errors bubble up to the global handler.
# Only set params that differ from defaults.
# Only set user_message if the user needs to take action.

raise BotspotError("Data validation failed")

raise BotspotError(
    message="Invalid format",
    user_message="Please use DD/MM/YYYY format",
)
```

There is no `botspot.errors` module — import `BotspotError` from `botspot.core.errors`.

## Optional Components Worth Knowing

- `event_scheduler`: `BOTSPOT_SCHEDULER_*`
- `queue_manager`: `BOTSPOT_QUEUE_MANAGER_*`
- `auto_archive`: `BOTSPOT_AUTO_ARCHIVE_*`
- `trial_mode`: `BOTSPOT_TRIAL_MODE_*` (legacy; billing trial is under subscription_manager)
- `telethon_manager`: `BOTSPOT_TELETHON_MANAGER_*`
- `s3_storage`, `message_aggregator`, `chat_fetcher`: matching env prefixes in `example.env`
