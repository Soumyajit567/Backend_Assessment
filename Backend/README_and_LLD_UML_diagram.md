    +--------------------+   (1) Register    +--------------------+
    |                    | <---------------- |                    |
    |       Client       |                   |      Users         |
    |                    |   (2) Get Users   |                    |
    +--------------------+ ----------------> | + id: int          |
            |                (3) Create      | + name: string     |
            |                Discussion      | + mobile_no: string|
            v                                | + email: string    |
    +--------------------+ ----------------> | + password: string |
    |   Discussions      | <---------------- |                    |
    |    Service         |   (4) View Users  +--------------------+
    +--------------------+                   ^           |
            |                                |           | (5) Fetch User
            v                                |           |
    +--------------------+                   |           v
    |    Comments        |   (6) Add Comment |    +--------------------+
    |    Service         | <---------------- |    |       Follows       |
    +--------------------+                   |    |                     |
            |                                |    | + id: int           |
            v                                |    | + follower_id: int  |
    +--------------------+                   |    | + followed_id: int  |
    |     Likes          |   (7) Like        |    |                     |
    |    Service         | <---------------- |    +---------------------+
    +--------------------+                   ^           |
            |                                |           |
            v                                |           v
    +--------------------+                   |    +---------------------+
    |     Follows        |   (8) Follow      |    |     Comments        |
    |    Service         | <---------------- |    |                     |
    +--------------------+                   |    | + id: int           |
                                             |    | + text: string      |
                                             |    | + user_id: int      |
                                             |    | + discussion_id: int|
                                             |    +---------------------+
                                             ^           |
                                             |           |
                                             |           v
                                             |    +---------------------+
                                             |    |      Discussions    |
                                             |    |                     |
                                             |    | + id: int           |
                                             |    | + text: string      |
                                             |    | + owner_id: int     |
                                             |    | + image: string     |
                                             |    | + hashtags: string  |
                                             |    +---------------------+




## Explanation of Data Flow

1. **Register**: The client sends a request to the Users service to register a new user.
2. **Get Users**: The client sends a request to the Users service to fetch a list of users.
3. **Create Discussion**: The client sends a request to the Discussions service to create a new discussion.
4. **View Users**: The Discussions service interacts with the Users service to view users.
5. **Fetch User**: The Follows service fetches user information from the Users service to validate follow relationships.
6. **Add Comment**: The client sends a request to the Comments service to add a comment to a discussion.
7. **Like**: The client sends a request to the Likes service to like a discussion or comment.
8. **Follow**: The client sends a request to the Follows service to follow another user.

## Services and Components

- **Client**: The frontend or client application that interacts with the backend services.
- **Users Service**: Manages user registration, authentication, and user-related data.
- **Discussions Service**: Manages creation and retrieval of discussions.
- **Comments Service**: Manages comments on discussions.
- **Likes Service**: Manages likes on discussions and comments.
- **Follows Service**: Manages following relationships between users.

## Relationships

- **Users and Discussions**: Discussions are created by users.
- **Users and Comments**: Comments are added by users to discussions.
- **Users and Likes**: Likes can be added by users to discussions and comments.
- **Users and Follows**: Users can follow other users.

## Interaction

- The client interacts with the backend services to perform actions such as creating users, discussions, comments, likes, and follow relationships.
- The services communicate with each other to manage the data flow and ensure data consistency across the system.