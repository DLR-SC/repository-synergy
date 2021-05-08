# MySQL CollectD Plugin

A python MySQL plugin for CollectD. Designed for MySQL 5.5+, and specifically variants such as MariaDB or Percona Server.

Pulls most of the same metrics as the Percona Monitoring Plugins for Cacti. Collects over 350 MySQL metrics per interval.

Most MySQL monitoring plugins fetch a lot of information by parsing the output of `SHOW ENGINE INNODB STATUS`. This plugin prefers InnoDB statistics from `SHOW GLOBAL STATUS`. Percona Server and MariaDB provide most of these InnoDB metrics on `SHOW GLOBAL STATUS`.

Requires the Python MySQLdb package. (`python-mysqldb` on Debian)

## Installation
1. Place mysql.py in your CollectD python plugins directory
2. Configure the plugin in CollectD
3. Restart CollectD

## Configuration
If you don’t already have the Python module loaded, you need to configure it first:

    <LoadPlugin python>
    	Globals true
    </LoadPlugin>
    <Plugin python>
    	ModulePath "/path/to/python/modules"
    </Plugin>

You should then configure the MySQL plugin:

	<Plugin python>
		Import mysql
		<Module mysql>
			Host "localhost" (default: localhost)
			Port 3306 (default: 3306)
			User "root" (default: root)
			Password "xxxx" (default: empty)
			HeartbeatTable "percona.heartbeat" (if using pt-heartbeat to track slave lag)
			Verbose false (default: false)
		</Module>
	</Plugin>

## Metrics

### MySQL Status

    status.Com_*
    status.Handler_*
    status.Aborted_clients
    status.Aborted_connects
    status.Binlog_cache_disk_use
    status.Binlog_cache_use
    status.Bytes_received
    status.Bytes_sent
    status.Connections
    status.Created_tmp_disk_tables
    status.Created_tmp_files
    status.Created_tmp_tables
    status.Innodb_buffer_pool_pages_data
    status.Innodb_buffer_pool_pages_dirty
    status.Innodb_buffer_pool_pages_free
    status.Innodb_buffer_pool_pages_total
    status.Innodb_buffer_pool_read_requests
    status.Innodb_buffer_pool_reads
    status.Innodb_checkpoint_age
    status.Innodb_data_fsyncs
    status.Innodb_data_pending_fsyncs
    status.Innodb_data_pending_reads
    status.Innodb_data_pending_writes
    status.Innodb_data_read
    status.Innodb_data_reads
    status.Innodb_data_writes
    status.Innodb_data_written
    status.Innodb_deadlocks
    status.Innodb_history_list_length
    status.Innodb_ibuf_free_list
    status.Innodb_ibuf_merged_delete_marks
    status.Innodb_ibuf_merged_deletes
    status.Innodb_ibuf_merged_inserts
    status.Innodb_ibuf_merges
    status.Innodb_ibuf_segment_size
    status.Innodb_ibuf_size
    status.Innodb_lsn_current
    status.Innodb_lsn_flushed
    status.Innodb_max_trx_id
    status.Innodb_mem_adaptive_hash
    status.Innodb_mem_dictionary
    status.Innodb_mem_total
    status.Innodb_mutex_os_waits
    status.Innodb_mutex_spin_rounds
    status.Innodb_mutex_spin_waits
    status.Innodb_os_log_pending_fsyncs
    status.Innodb_pages_created
    status.Innodb_pages_read
    status.Innodb_pages_written
    status.Innodb_row_lock_time
    status.Innodb_row_lock_time_avg
    status.Innodb_row_lock_time_max
    status.Innodb_row_lock_waits
    status.Innodb_rows_deleted
    status.Innodb_rows_inserted
    status.Innodb_rows_read
    status.Innodb_rows_updated
    status.Innodb_s_lock_os_waits
    status.Innodb_s_lock_spin_rounds
    status.Innodb_s_lock_spin_waits
    status.Innodb_x_lock_os_waits
    status.Innodb_x_lock_spin_rounds
    status.Innodb_x_lock_spin_waits
    status.Key_blocks_not_flushed
    status.Key_blocks_unused
    status.Key_blocks_used
    status.Key_read_requests
    status.Key_reads
    status.Key_write_requests
    status.Key_writes
    status.Max_used_connections
    status.Open_files
    status.Open_table_definitions
    status.Open_tables
    status.Opened_files
    status.Opened_table_definitions
    status.Opened_tables
    status.Qcache_free_blocks
    status.Qcache_free_memory
    status.Qcache_hits
    status.Qcache_inserts
    status.Qcache_lowmem_prunes
    status.Qcache_not_cached
    status.Qcache_queries_in_cache
    status.Qcache_total_blocks
    status.Questions
    status.Select_full_join
    status.Select_full_range_join
    status.Select_range
    status.Select_range_check
    status.Select_scan
    status.Slave_open_temp_tables
    status.Slave_retried_transactions
    status.Slow_launch_threads
    status.Slow_queries
    status.Sort_merge_passes
    status.Sort_range
    status.Sort_rows
    status.Sort_scan
    status.Table_locks_immediate
    status.Table_locks_waited
    status.Table_open_cache_hits
    status.Table_open_cache_misses
    status.Table_open_cache_overflows
    status.Threadpool_idle_threads
    status.Threadpool_threads
    status.Threads_cached
    status.Threads_connected
    status.Threads_created
    status.Threads_running
    status.Uptime


The following are determined programatically:

    status.Innodb_unpurged_txns = Innodb_max_trx_id - Innodb_purge_trx_id
    status.Innodb_uncheckpointed_bytes = Innodb_lsn_current - Innodb_lsn_last_checkpoint
    status.Innodb_unflushed_log = Innodb_lsn_current - Innodb_lsn_flushed

### MySQL Variables

Collected from `SHOW VARIABLES`:

    variables.binlog_stmt_cache_size
    variables.innodb_additional_mem_pool_size
    variables.innodb_buffer_pool_size
    variables.innodb_concurrency_tickets
    variables.innodb_io_capacity
    variables.innodb_log_buffer_size
    variables.innodb_log_file_size
    variables.innodb_open_files
    variables.innodb_open_files
    variables.join_buffer_size
    variables.max_connections
    variables.open_files_limit
    variables.query_cache_limit
    variables.query_cache_size
    variables.query_cache_size
    variables.read_buffer_size
    variables.table_cache
    variables.table_definition_cache
    variables.table_open_cache
    variables.thread_cache_size
    variables.thread_cache_size
    variables.thread_concurrency
    variables.tmp_table_size

### MySQL Processes

Count of MySQL processes from `SHOW PROCESSLIST` grouped by state:

    state.closing_tables
    state.copying_to_tmp_table
    state.end
    state.freeing_items
    state.init
    state.locked
    state.login
    state.none
    state.preparing
    state.reading_from_net
    state.sending_data
    state.sorting_result
    state.statistics
    state.updating
    state.writing_to_net
    state.other - All other states

### InnoDB Status

Collected by parsing the output of `SHOW ENGINE INNODB STATUS`:

    innodb.active_transactions
    innodb.current_transactions
    innodb.file_reads
    innodb.file_system_memory
    innodb.file_writes
    innodb.innodb_lock_structs
    innodb.innodb_lock_wait_secs
    innodb.innodb_locked_tables
    innodb.innodb_sem_wait_time_ms
    innodb.innodb_sem_waits
    innodb.innodb_tables_in_use
    innodb.lock_system_memory
    innodb.locked_transactions
    innodb.log_writes
    innodb.page_hash_memory
    innodb.pending_aio_log_ios
    innodb.pending_buf_pool_flushes
    innodb.pending_chkp_writes
    innodb.pending_ibuf_aio_reads
    innodb.pending_log_writes
    innodb.queries_inside
    innodb.queries_queued
    innodb.read_views

In addition, the following InnoDB status variables which would normally be collected by parsing `SHOW ENGINE INNODB STATUS` in Percona's Cacti monitoring plugin are collected from`SHOW GLOBAL STATUS`:

	spin_waits
		Innodb_mutex_spin_waits
		Innodb_s_lock_spin_waits
		Innodb_x_lock_spin_waits
	spin_rounds
		Innodb_mutex_spin_rounds
		Innodb_s_lock_spin_rounds
		Innodb_x_lock_spin_rounds
	os_waits
		Innodb_mutex_os_waits
		Innodb_x_lock_os_waits
	pending_normal_aio_reads - Innodb_data_pending_reads
	pending_normal_aio_writes - Innodb_data_pending_writes
	pending_log_flushes - Innodb_os_log_pending_fsyncs
	file_fsyncs - Innodb_data_fsyncs
	ibuf_inserts - Innodb_ibuf_merged_inserts
	ibuf_merged
		Innodb_ibuf_merged_inserts
		Innodb_ibuf_merged_deletes
		Innodb_ibuf_merged_delete_marks
	ibuf_merges - Innodb_ibuf_merges
	log_bytes_written - Innodb_lsn_current
	log_bytes_flushed - Innodb_lsn_flushed
	pool_size - Innodb_buffer_pool_pages_total
	free_pages - Innodb_buffer_pool_pages_free
	database_pages - Innodb_buffer_pool_pages_data
	modified_pages - Innodb_buffer_pool_pages_dirty
	pages_read - Innodb_pages_read
	pages_created - Innodb_pages_created
	pages_written - Innodb_pages_written
	rows_inserted - Innodb_rows_inserted
	rows_updated - Innodb_rows_updated
	rows_deleted - Innodb_rows_deleted
	rows_read - Innodb_rows_read
	unpurged_txns - Innodb_unpurged_txns
	history_list - Innodb_history_list_length
	last_checkpoint - Innodb_lsn_last_checkpoint
	ibuf_used_cells - Innodb_ibuf_size
	ibuf_free_cells - Innodb_ibuf_free_list
	ibuf_cell_count - Innodb_ibuf_segment_size
	adaptive_hash_memory - Innodb_mem_adaptive_hash
	dictionary_cache_memory - Innodb_mem_dictionary
	unflushed_log - Innodb_unflushed_log
	uncheckpointed_bytes - Innodb_uncheckpointed_bytes
	pool_reads - Innodb_buffer_pool_reads
	pool_read_requests - Innodb_buffer_pool_read_requests
	innodb_transactions - Innodb_max_trx_id
	total_mem_alloc - Innodb_mem_total


TBD:

	pending_aio_sync_ios
	hash_index_cells_total
	hash_index_cells_used
	additional_pool_alloc


### Master/Slave Status
   
From `SHOW BINARY LOGS`:

    master.binary_log_space - Total file size consumed by binlog files

From `SHOW SLAVE STATUS`:

	slave.relay_log_space - Total file size consumed by relay log files
    slave.slave_lag - Value of Seconds_Behind_Master, unless using HeartbeatTable is supplied, in which case slave lag will be determined from the pt-heartbeat table based on the server's master server ID.
    slave.slave_stopped - 1 when the slave is stopped, 0 when it's running
    slave.slave_running - 1 when the slave is running, 0 when it's stopped

### Query Response Times

For versions of MySQL with support for it and where enabled, `INFORMATION_SCHEMA.QUERY_RESPONSE_TIME` will be queried for metrics to generate a histogram of query response times.

[Additional information on response time histograms in Percona Server](http://www.percona.com/blog/2010/07/11/query-response-time-histogram-new-feature-in-percona-server/)

    response_time_total.1
    response_time_count.1
    ...
    response_time_total.14
    response_time_count.14

## License
MIT (http://www.opensource.org/licenses/mit-license.php)
