[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/yangkyeongmo-mcp-server-openmetadata-badge.png)](https://mseep.ai/app/yangkyeongmo-mcp-server-openmetadata)

# mcp-server-openmetadata

[![LightNow capabilities](https://lightnow.ai/badge/io.github.yangkyeongmo/mcp-server-openmetadata)](https://lightnow.ai/servers/io.github.yangkyeongmo/mcp-server-openmetadata)

A Model Context Protocol (MCP) server implementation for OpenMetadata, enabling seamless integration with MCP clients. This project provides a standardized way to interact with OpenMetadata through the Model Context Protocol.

<a href="https://glama.ai/mcp/servers/lvgl5cmxa6">
  <img width="380" height="200" src="https://glama.ai/mcp/servers/lvgl5cmxa6/badge" alt="Server for OpenMetadata MCP server" />
</a>

## About

This project implements a [Model Context Protocol](https://modelcontextprotocol.io/introduction) server that wraps OpenMetadata's REST API, allowing MCP clients to interact with OpenMetadata in a standardized way.

## Feature Implementation Status

### Core Data Entities (`table`, `database`, `databaseschema`)

| Feature | API Path | Status |
|---------|----------|--------|
| **Tables** | | |
| List Tables | `/api/v1/tables` | ✅ |
| Get Table | `/api/v1/tables/{id}` | ✅ |
| Get Table by Name | `/api/v1/tables/name/{fqn}` | ✅ |
| Create Table | `/api/v1/tables` | ✅ |
| Update Table | `/api/v1/tables/{id}` | ✅ |
| Delete Table | `/api/v1/tables/{id}` | ✅ |
| **Databases** | | |
| List Databases | `/api/v1/databases` | ✅ |
| Get Database | `/api/v1/databases/{id}` | ✅ |
| Get Database by Name | `/api/v1/databases/name/{fqn}` | ✅ |
| Create Database | `/api/v1/databases` | ✅ |
| Update Database | `/api/v1/databases/{id}` | ✅ |
| Delete Database | `/api/v1/databases/{id}` | ✅ |
| **Database Schemas** | | |
| List Database Schemas | `/api/v1/databaseSchemas` | ✅ |
| Get Database Schema | `/api/v1/databaseSchemas/{id}` | ✅ |
| Get Database Schema by Name | `/api/v1/databaseSchemas/name/{fqn}` | ✅ |
| Create Database Schema | `/api/v1/databaseSchemas` | ✅ |
| Update Database Schema | `/api/v1/databaseSchemas/{id}` | ✅ |
| Delete Database Schema | `/api/v1/databaseSchemas/{id}` | ✅ |

### Data Assets (`dashboard`, `chart`, `pipeline`, `topic`, `metric`, `container`, `report`, `mlmodel`)

| Feature | API Path | Status |
|---------|----------|--------|
| **Dashboards** | | |
| List Dashboards | `/api/v1/dashboards` | ✅ |
| Get Dashboard | `/api/v1/dashboards/{id}` | ✅ |
| Get Dashboard by Name | `/api/v1/dashboards/name/{fqn}` | ✅ |
| Create Dashboard | `/api/v1/dashboards` | ✅ |
| Update Dashboard | `/api/v1/dashboards/{id}` | ✅ |
| Delete Dashboard | `/api/v1/dashboards/{id}` | ✅ |
| **Charts** | | |
| List Charts | `/api/v1/charts` | ✅ |
| Get Chart | `/api/v1/charts/{id}` | ✅ |
| Get Chart by Name | `/api/v1/charts/name/{fqn}` | ✅ |
| Create Chart | `/api/v1/charts` | ✅ |
| Update Chart | `/api/v1/charts/{id}` | ✅ |
| Delete Chart | `/api/v1/charts/{id}` | ✅ |
| **Pipelines** | | |
| List Pipelines | `/api/v1/pipelines` | ✅ |
| Get Pipeline | `/api/v1/pipelines/{id}` | ✅ |
| Get Pipeline by Name | `/api/v1/pipelines/name/{fqn}` | ✅ |
| Create Pipeline | `/api/v1/pipelines` | ✅ |
| Update Pipeline | `/api/v1/pipelines/{id}` | ✅ |
| Delete Pipeline | `/api/v1/pipelines/{id}` | ✅ |
| **Topics** | | |
| List Topics | `/api/v1/topics` | ✅ |
| Get Topic | `/api/v1/topics/{id}` | ✅ |
| Get Topic by Name | `/api/v1/topics/name/{fqn}` | ✅ |
| Create Topic | `/api/v1/topics` | ✅ |
| Update Topic | `/api/v1/topics/{id}` | ✅ |
| Delete Topic | `/api/v1/topics/{id}` | ✅ |
| **Metrics** | | |
| List Metrics | `/api/v1/metrics` | ✅ |
| Get Metric | `/api/v1/metrics/{id}` | ✅ |
| Get Metric by Name | `/api/v1/metrics/name/{fqn}` | ✅ |
| Create Metric | `/api/v1/metrics` | ✅ |
| Update Metric | `/api/v1/metrics/{id}` | ✅ |
| Delete Metric | `/api/v1/metrics/{id}` | ✅ |
| **Containers** | | |
| List Containers | `/api/v1/containers` | ✅ |
| Get Container | `/api/v1/containers/{id}` | ✅ |
| Get Container by Name | `/api/v1/containers/name/{fqn}` | ✅ |
| Create Container | `/api/v1/containers` | ✅ |
| Update Container | `/api/v1/containers/{id}` | ✅ |
| Delete Container | `/api/v1/containers/{id}` | ✅ |
| **Reports** | | |
| List Reports | `/api/v1/reports` | ✅ |
| Get Report | `/api/v1/reports/{id}` | ✅ |
| Get Report by Name | `/api/v1/reports/name/{fqn}` | ✅ |
| Create Report | `/api/v1/reports` | ✅ |
| Update Report | `/api/v1/reports/{id}` | ✅ |
| Delete Report | `/api/v1/reports/{id}` | ✅ |
| **ML Models** | | |
| List ML Models | `/api/v1/mlmodels` | ✅ |
| Get ML Model | `/api/v1/mlmodels/{id}` | ✅ |
| Get ML Model by Name | `/api/v1/mlmodels/name/{fqn}` | ✅ |
| Create ML Model | `/api/v1/mlmodels` | ✅ |
| Update ML Model | `/api/v1/mlmodels/{id}` | ✅ |
| Delete ML Model | `/api/v1/mlmodels/{id}` | ✅ |

### Users & Teams (`user`, `team`)

| Feature | API Path | Status |
|---------|----------|--------|
| **Teams** | | |
| List Teams | `/api/v1/teams` | ✅ |
| Get Team | `/api/v1/teams/{id}` | ✅ |
| Get Team by Name | `/api/v1/teams/name/{name}` | ✅ |
| Create Team | `/api/v1/teams` | ✅ |
| Update Team | `/api/v1/teams/{id}` | ✅ |
| Delete Team | `/api/v1/teams/{id}` | ✅ |
| **Users** | | |
| List Users | `/api/v1/users` | ✅ |
| Get User | `/api/v1/users/{id}` | ✅ |
| Get User by Name | `/api/v1/users/name/{name}` | ✅ |
| Create User | `/api/v1/users` | ✅ |
| Update User | `/api/v1/users/{id}` | ✅ |
| Delete User | `/api/v1/users/{id}` | ✅ |

### Governance & Classification (`classification`, `glossary`, `tag`)

| Feature | API Path | Status |
|---------|----------|--------|
| **Classifications** | | |
| List Classifications | `/api/v1/classifications` | ✅ |
| Get Classification | `/api/v1/classifications/{id}` | ✅ |
| Get Classification by Name | `/api/v1/classifications/name/{name}` | ✅ |
| Create Classification | `/api/v1/classifications` | ✅ |
| Update Classification | `/api/v1/classifications/{id}` | ✅ |
| Delete Classification | `/api/v1/classifications/{id}` | ✅ |
| **Glossaries** | | |
| List Glossaries | `/api/v1/glossaries` | ✅ |
| Get Glossary | `/api/v1/glossaries/{id}` | ✅ |
| Get Glossary by Name | `/api/v1/glossaries/name/{name}` | ✅ |
| Create Glossary | `/api/v1/glossaries` | ✅ |
| Update Glossary | `/api/v1/glossaries/{id}` | ✅ |
| Delete Glossary | `/api/v1/glossaries/{id}` | ✅ |
| List Glossary Terms | `/api/v1/glossaryTerms` | ✅ |
| Get Glossary Term | `/api/v1/glossaryTerms/{id}` | ✅ |
| **Tags** | | |
| List Tags | `/api/v1/tags` | ✅ |
| Get Tag | `/api/v1/tags/{id}` | ✅ |
| Get Tag by Name | `/api/v1/tags/name/{name}` | ✅ |
| Create Tag | `/api/v1/tags` | ✅ |
| Update Tag | `/api/v1/tags/{id}` | ✅ |
| Delete Tag | `/api/v1/tags/{id}` | ✅ |

### System & Operations (`bot`, `services`, `event`)

| Feature | API Path | Status |
|---------|----------|--------|
| **Bots** | | |
| List Bots | `/api/v1/bots` | ✅ |
| Get Bot | `/api/v1/bots/{id}` | ✅ |
| Get Bot by Name | `/api/v1/bots/name/{name}` | ✅ |
| Create Bot | `/api/v1/bots` | ✅ |
| Update Bot | `/api/v1/bots/{id}` | ✅ |
| Delete Bot | `/api/v1/bots/{id}` | ✅ |
| **Services** | | |
| List Services | `/api/v1/services` | ✅ |
| Database Services | `/api/v1/services/databaseServices` | ✅ |
| Dashboard Services | `/api/v1/services/dashboardServices` | ✅ |
| Messaging Services | `/api/v1/services/messagingServices` | ✅ |
| Test Connection | `/api/v1/services/testConnection` | ✅ |
| **Events** | | |
| List Events | `/api/v1/events` | ✅ |
| List Event Subscriptions | `/api/v1/events/subscriptions` | ✅ |
| Get Event Subscription | `/api/v1/events/subscriptions/{id}` | ✅ |
| Create Event Subscription | `/api/v1/events/subscriptions` | ✅ |
| Update Event Subscription | `/api/v1/events/subscriptions/{id}` | ✅ |
| Delete Event Subscription | `/api/v1/events/subscriptions/{id}` | ✅ |
| Test Destination | `/api/v1/events/subscriptions/testDestination` | ✅ |

### Analytics & Monitoring (`lineage`, `usage`, `search`)

| Feature | API Path | Status |
|---------|----------|--------|
| **Lineage** | | |
| Get Lineage by Entity ID | `/api/v1/lineage/{entity}/{id}` | ✅ |
| Get Lineage by Entity Name | `/api/v1/lineage/{entity}/name/{fqn}` | ✅ |
| Add/Update Lineage | `/api/v1/lineage` | ✅ |
| Delete Lineage | `/api/v1/lineage` | ✅ |
| **Usage** | | |
| Get Entity Usage | `/api/v1/usage/{entity}/{id}` | ✅ |
| Add Usage Data | `/api/v1/usage` | ✅ |
| Get Usage Summary | `/api/v1/usage/summary` | ✅ |
| **Search & Discovery** | | |
| Search Query | `/api/v1/search/query` | ✅ |
| Search Suggest | `/api/v1/search/suggest` | ✅ |
| Search Aggregate | `/api/v1/search/aggregate` | ✅ |
| Search Field Query | `/api/v1/search/fieldQuery` | ✅ |

### Data Quality (`test_case`, `test_suite`)

| Feature | API Path | Status |
|---------|----------|--------|
| **Test Cases** | | |
| List Test Cases | `/api/v1/dataQuality/testCases` | ✅ |
| Get Test Case | `/api/v1/dataQuality/testCases/{id}` | ✅ |
| Get Test Case by Name | `/api/v1/dataQuality/testCases/name/{fqn}` | ✅ |
| Create Test Case | `/api/v1/dataQuality/testCases` | ✅ |
| Update Test Case | `/api/v1/dataQuality/testCases/{id}` | ✅ |
| Delete Test Case | `/api/v1/dataQuality/testCases/{id}` | ✅ |
| List Test Case Results | `/api/v1/dataQuality/testCases/{fqn}/testCaseResult` | ✅ |
| Get Test Case Results | `/api/v1/dataQuality/testCases/testCaseResults/{fqn}` | ✅ |
| **Test Suites** | | |
| List Test Suites | `/api/v1/dataQuality/testSuites` | ✅ |
| Get Test Suite | `/api/v1/dataQuality/testSuites/{id}` | ✅ |
| Get Test Suite by Name | `/api/v1/dataQuality/testSuites/name/{name}` | ✅ |
| Create Basic Test Suite | `/api/v1/dataQuality/testSuites/basic` | ✅ |
| Create Executable Test Suite | `/api/v1/dataQuality/testSuites/executable` | ✅ |
| Update Test Suite | `/api/v1/dataQuality/testSuites/{id}` | ✅ |
| Delete Test Suite | `/api/v1/dataQuality/testSuites/{id}` | ✅ |
| Get Execution Summary | `/api/v1/dataQuality/testSuites/executionSummary` | ✅ |
| Get Data Quality Report | `/api/v1/dataQuality/testSuites/dataQualityReport` | ✅ |

### Access Control & Security (`policy`, `role`)

| Feature | API Path | Status |
|---------|----------|--------|
| **Policies** | | |
| List Policies | `/api/v1/policies` | ✅ |
| Get Policy | `/api/v1/policies/{id}` | ✅ |
| Get Policy by Name | `/api/v1/policies/name/{name}` | ✅ |
| Create Policy | `/api/v1/policies` | ✅ |
| Update Policy | `/api/v1/policies/{id}` | ✅ |
| Delete Policy | `/api/v1/policies/{id}` | ✅ |
| Validate Policy | `/api/v1/policies/validation/condition` | ✅ |
| List Policy Resources | `/api/v1/policies/resources` | ✅ |
| **Roles** | | |
| List Roles | `/api/v1/roles` | ✅ |
| Get Role | `/api/v1/roles/{id}` | ✅ |
| Get Role by Name | `/api/v1/roles/name/{name}` | ✅ |
| Create Role | `/api/v1/roles` | ✅ |
| Update Role | `/api/v1/roles/{id}` | ✅ |
| Delete Role | `/api/v1/roles/{id}` | ✅ |

### Domain Management (`domain`)

| Feature | API Path | Status |
|---------|----------|--------|
| **Domains** | | |
| List Domains | `/api/v1/domains` | ✅ |
| Get Domain | `/api/v1/domains/{id}` | ✅ |
| Get Domain by Name | `/api/v1/domains/name/{name}` | ✅ |
| Create Domain | `/api/v1/domains` | ✅ |
| Update Domain | `/api/v1/domains/{id}` | ✅ |
| Delete Domain | `/api/v1/domains/{id}` | ✅ |
| **Data Products** | | |
| List Data Products | `/api/v1/dataProducts` | ✅ |
| Get Data Product | `/api/v1/dataProducts/{id}` | ✅ |
| Get Data Product by Name | `/api/v1/dataProducts/name/{fqn}` | ✅ |
| Create Data Product | `/api/v1/dataProducts` | ✅ |
| Update Data Product | `/api/v1/dataProducts/{id}` | ✅ |
| Delete Data Product | `/api/v1/dataProducts/{id}` | ✅ |

### Not Yet Implemented

| Feature | API Path | Status |
|---------|----------|--------|
| **API Management** | | |
| API Collections | `/api/v1/apiCollections` | ❌ |
| API Endpoints | `/api/v1/apiEndpoints` | ❌ |
| **Other Assets** | | |
| Apps | `/api/v1/apps` | ❌ |
| **Feeds & Activity** | | |
| Feeds | `/api/v1/feed` | ❌ |
| **Advanced Features** | | |
| Personas | `/api/v1/personas` | ❌ |
| Queries | `/api/v1/queries` | ❌ |
| Search Indexes | `/api/v1/searchIndexes` | ❌ |
| Stored Procedures | `/api/v1/storedProcedures` | ❌ |
| Suggestions | `/api/v1/suggestions` | ❌ |
| Webhooks | `/api/v1/webhooks` | ❌ |

## API Groups

The server supports modular API group selection via command line arguments. Available API groups:

### Core Data Entities
- `table` - Table entity management
- `database` - Database entity management  
- `databaseschema` - Database schema management

### Data Assets
- `dashboard` - Dashboard entity management
- `chart` - Chart entity management
- `pipeline` - Pipeline entity management
- `topic` - Topic entity management
- `metrics` - Metric entity management
- `container` - Container entity management
- `report` - Report entity management
- `mlmodel` - ML Model entity management

### Users & Teams
- `user` - User entity management
- `team` - Team entity management

### Governance & Classification
- `classification` - Classification entity management
- `glossary` - Glossary and glossary terms management
- `tag` - Tag and tag category management

### System & Operations
- `bot` - Bot entity management
- `services` - Service configurations and connection testing
- `event` - Event subscriptions and notifications

### Analytics & Monitoring
- `lineage` - Data lineage management
- `usage` - Usage analytics management
- `search` - Search and discovery operations

### Data Quality
- `test_case` - Data quality test case management
- `test_suite` - Data quality test suite management

### Access Control & Security
- `policy` - Access policies and security management
- `role` - Role-based access control management

### Domain Management
- `domain` - Domain and data product management

You can specify which API groups to enable when running the server:

```bash
# Enable only core entities
python -m src.main --apis table,database,databaseschema

# Enable comprehensive data quality and governance
python -m src.main --apis test_case,test_suite,policy,role,tag,domain

# Enable all available APIs
python -m src.main --apis table,database,databaseschema,dashboard,chart,pipeline,topic,metrics,container,report,mlmodel,user,team,classification,glossary,tag,bot,services,event,lineage,usage,search,test_case,test_suite,policy,role,domain

# Use default selection (all implemented APIs)
python -m src.main
```

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
