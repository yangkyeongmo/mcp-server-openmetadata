# mcp-server-openmetadata

[![smithery badge](https://smithery.ai/badge/@yangkyeongmo/mcp-server-openmetadata)](https://smithery.ai/server/@yangkyeongmo/mcp-server-openmetadata)

A Model Context Protocol (MCP) server implementation for OpenMetadata, enabling seamless integration with MCP clients. This project provides a standardized way to interact with OpenMetadata through the Model Context Protocol.

## About

This project implements a [Model Context Protocol](https://modelcontextprotocol.io/introduction) server that wraps OpenMetadata's REST API, allowing MCP clients to interact with OpenMetadata in a standardized way.

## Feature Implementation Status

| Feature | API Path | Status |
|---------|----------|--------|
| **Data Assets** | | |
| List Databases | `/api/v1/databases` | ❌ |
| Get Database | `/api/v1/databases/{id}` | ❌ |
| Get Database by Name | `/api/v1/databases/name/{fqn}` | ❌ |
| Export Database | `/api/v1/databases/name/{name}/export` | ❌ |
| Import Database | `/api/v1/databases/name/{name}/import` | ❌ |
| List Tables | `/api/v1/tables` | ✅ |
| Get Table | `/api/v1/tables/{id}` | ✅ |
| Get Table by Name | `/api/v1/tables/name/{fqn}` | ✅ |
| Create Table | `/api/v1/tables` | ✅ |
| Update Table | `/api/v1/tables/{id}` | ✅ |
| Delete Table | `/api/v1/tables/{id}` | ✅ |
| Export Table | `/api/v1/tables/name/{name}/export` | ❌ |
| Import Table | `/api/v1/tables/name/{name}/import` | ❌ |
| List Metrics | `/api/v1/metrics` | ❌ |
| Get Metric | `/api/v1/metrics/{id}` | ❌ |
| List Dashboards | `/api/v1/dashboards` | ❌ |
| Get Dashboard | `/api/v1/dashboards/{id}` | ❌ |
| Get Dashboard by Name | `/api/v1/dashboards/name/{fqn}` | ❌ |
| List Reports | `/api/v1/reports` | ❌ |
| Get Report | `/api/v1/reports/{id}` | ❌ |
| List Pipelines | `/api/v1/pipelines` | ❌ |
| Get Pipeline | `/api/v1/pipelines/{id}` | ❌ |
| Get Pipeline by Name | `/api/v1/pipelines/name/{fqn}` | ❌ |
| List Topics | `/api/v1/topics` | ❌ |
| Get Topic | `/api/v1/topics/{id}` | ❌ |
| **Services** | | |
| List Database Services | `/api/v1/services/databaseServices` | ❌ |
| Get Database Service | `/api/v1/services/databaseServices/{id}` | ❌ |
| Get Database Service by Name | `/api/v1/services/databaseServices/name/{fqn}` | ❌ |
| Export Database Service | `/api/v1/services/databaseServices/name/{name}/export` | ❌ |
| Import Database Service | `/api/v1/services/databaseServices/name/{name}/import` | ❌ |
| List Dashboard Services | `/api/v1/services/dashboardServices` | ❌ |
| Get Dashboard Service | `/api/v1/services/dashboardServices/{id}` | ❌ |
| Get Dashboard Service by Name | `/api/v1/services/dashboardServices/name/{fqn}` | ❌ |
| **Teams & Users** | | |
| List Teams | `/api/v1/teams` | ❌ |
| Get Team | `/api/v1/teams/{id}` | ❌ |
| Get Team by Name | `/api/v1/teams/name/{fqn}` | ❌ |
| Export Team | `/api/v1/teams/name/{name}/export` | ❌ |
| Import Team | `/api/v1/teams/name/{name}/import` | ❌ |
| List Users | `/api/v1/users` | ❌ |
| Get User | `/api/v1/users/{id}` | ❌ |
| Get User by Name | `/api/v1/users/name/{name}` | ❌ |
| User Login | `/api/v1/users/login` | ❌ |
| User Logout | `/api/v1/users/logout` | ❌ |
| User Signup | `/api/v1/users/signup` | ❌ |
| Change Password | `/api/v1/users/changePassword` | ❌ |
| **Search** | | |
| Search Query | `/api/v1/search/query` | ❌ |
| Search Suggest | `/api/v1/search/suggest` | ❌ |
| Search Aggregate | `/api/v1/search/aggregate` | ❌ |
| Field Query | `/api/v1/search/fieldQuery` | ❌ |
| Get Document | `/api/v1/search/get/{index}/doc/{id}` | ❌ |
| **Tags & Classifications** | | |
| List Tags | `/api/v1/tags` | ❌ |
| Get Tag | `/api/v1/tags/{id}` | ❌ |
| Get Tag by Name | `/api/v1/tags/name/{fqn}` | ❌ |
| **Lineage** | | |
| Get Lineage | `/api/v1/lineage/getLineage` | ❌ |
| Export Lineage | `/api/v1/lineage/export` | ❌ |
| Get Entity Lineage by Name | `/api/v1/lineage/{entity}/name/{fqn}` | ❌ |
| Get Entity Lineage by ID | `/api/v1/lineage/{entity}/{id}` | ❌ |
| Get Lineage Edge | `/api/v1/lineage/getLineageEdge/{fromId}/{toId}` | ❌ |
| Add/Update Lineage | `/api/v1/lineage` | ❌ |
| Add/Update Lineage by FQN | `/api/v1/lineage/{fromEntity}/name/{fromFQN}/{toEntity}/name/{toFQN}` | ❌ |
| Add/Update Lineage by ID | `/api/v1/lineage/{fromEntity}/{fromId}/{toEntity}/{toId}` | ❌ |
| **Glossaries** | | |
| List Glossaries | `/api/v1/glossaries` | ❌ |
| Get Glossary | `/api/v1/glossaries/{id}` | ❌ |
| Get Glossary by Name | `/api/v1/glossaries/name/{fqn}` | ❌ |
| Export Glossary | `/api/v1/glossaries/name/{name}/export` | ❌ |
| Import Glossary | `/api/v1/glossaries/name/{name}/import` | ❌ |
| List Glossary Terms | `/api/v1/glossaryTerms` | ❌ |
| Get Glossary Term | `/api/v1/glossaryTerms/{id}` | ❌ |
| Get Glossary Term by Name | `/api/v1/glossaryTerms/name/{fqn}` | ❌ |
| Add Assets to Term | `/api/v1/glossaryTerms/{id}/assets/add` | ❌ |
| Remove Assets from Term | `/api/v1/glossaryTerms/{id}/assets/remove` | ❌ |
| Validate Term Tags | `/api/v1/glossaryTerms/{id}/tags/validate` | ❌ |
| **Usage** | | |
| Get Entity Usage by Name | `/api/v1/usage/{entity}/name/{fqn}` | ❌ |
| Get Entity Usage by ID | `/api/v1/usage/{entity}/{id}` | ❌ |

## Setup

### Installing via Smithery

To install OpenMetadata MCP Server for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@yangkyeongmo/mcp-server-openmetadata):

```bash
npx -y @smithery/cli install @yangkyeongmo/mcp-server-openmetadata --client claude
```

### Environment Variables

Set one of the following authentication methods:

#### Token Authentication (Recommended)
```
OPENMETADATA_HOST=<your-openmetadata-host>
OPENMETADATA_JWT_TOKEN=<your-jwt-token>
```

#### Basic Authentication
```
OPENMETADATA_HOST=<your-openmetadata-host>
OPENMETADATA_USERNAME=<your-username>
OPENMETADATA_PASSWORD=<your-password>
```

### Usage with Claude Desktop

Add to your `claude_desktop_config.json` using one of the following authentication methods:

#### Token Authentication (Recommended)
```json
{
  "mcpServers": {
    "mcp-server-openmetadata": {
      "command": "uvx",
      "args": ["mcp-server-openmetadata"],
      "env": {
        "OPENMETADATA_HOST": "https://your-openmetadata-host",
        "OPENMETADATA_JWT_TOKEN": "your-jwt-token"
      }
    }
  }
}
```

#### Basic Authentication
```json
{
  "mcpServers": {
    "mcp-server-openmetadata": {
      "command": "uvx",
      "args": ["mcp-server-openmetadata"],
      "env": {
        "OPENMETADATA_HOST": "https://your-openmetadata-host",
        "OPENMETADATA_USERNAME": "your-username",
        "OPENMETADATA_PASSWORD": "your-password"
      }
    }
  }
}
```

Alternative configuration using `uv`:

#### Token Authentication (Recommended)
```json
{
  "mcpServers": {
    "mcp-server-openmetadata": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/mcp-server-openmetadata",
        "run",
        "mcp-server-openmetadata"
      ],
      "env": {
        "OPENMETADATA_HOST": "https://your-openmetadata-host",
        "OPENMETADATA_JWT_TOKEN": "your-jwt-token"
      }
    }
  }
}
```

#### Basic Authentication
```json
{
  "mcpServers": {
    "mcp-server-openmetadata": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/mcp-server-openmetadata",
        "run",
        "mcp-server-openmetadata"
      ],
      "env": {
        "OPENMETADATA_HOST": "https://your-openmetadata-host",
        "OPENMETADATA_USERNAME": "your-username",
        "OPENMETADATA_PASSWORD": "your-password"
      }
    }
  }
}
```

Replace `/path/to/mcp-server-openmetadata` with the actual path where you've cloned the repository.

### Manual Execution

You can also run the server manually:
```bash
python src/server.py
```

Options:
- `--port`: Port to listen on for SSE (default: 8000)
- `--transport`: Transport type (stdio/sse, default: stdio)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License
