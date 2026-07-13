from enum import StrEnum

class APITags(StrEnum):
    HEALTH = "Health"
    AUTH = "Authentication"
    USERS = "Users"
    DOCUMENTS = "Documents"
    CHAT = "Chat"
    ADMIN = "Admin"