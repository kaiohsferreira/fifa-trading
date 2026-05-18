const fs = require('fs');
const path = require('path');

const memoryDir = path.join(__dirname, '../memory');
const archivesDir = path.join(memoryDir, 'archives');

if (!fs.existsSync(archivesDir)) {
    fs.mkdirSync(archivesDir, { recursive: true });
}

const currentDate = new Date();
const currentYear = currentDate.getFullYear();
const currentQuarter = Math.floor((currentDate.getMonth() + 3) / 3);
const archiveSuffix = `Q${currentQuarter}-${currentYear}`;

// ----- Arquivar 06-implementation-log.md -----
function archiveImplementationLog() {
    const filePath = path.join(memoryDir, '06-implementation-log.md');
    const archivePath = path.join(archivesDir, `06-implementation-log-archive-${archiveSuffix}.md`);
    
    if (!fs.existsSync(filePath)) return;
    
    const content = fs.readFileSync(filePath, 'utf8');
    const lines = content.split('\n');
    
    let activeLines = [];
    let archiveLines = [];
    
    let currentBlock = [];
    let isOldBlock = false;
    
    const fifteenDaysAgo = new Date();
    fifteenDaysAgo.setDate(fifteenDaysAgo.getDate() - 15);
    
    // Check if file starts with a header
    let headerLength = 0;
    while(headerLength < lines.length && !lines[headerLength].startsWith('Data:')) {
        activeLines.push(lines[headerLength]);
        if (!fs.existsSync(archivePath)) {
            archiveLines.push(lines[headerLength]);
        }
        headerLength++;
    }

    for (let i = headerLength; i < lines.length; i++) {
        const line = lines[i];
        if (line.startsWith('Data:')) {
            // Process previous block
            if (currentBlock.length > 0) {
                if (isOldBlock) {
                    archiveLines.push(...currentBlock);
                } else {
                    activeLines.push(...currentBlock);
                }
            }
            
            // Start new block
            currentBlock = [line];
            const dateMatch = line.match(/Data:\s*(\d{4}-\d{2}-\d{2})/);
            if (dateMatch) {
                const blockDate = new Date(dateMatch[1]);
                isOldBlock = blockDate < fifteenDaysAgo;
            } else {
                isOldBlock = false; // preserve if no date found
            }
        } else {
            currentBlock.push(line);
        }
    }
    
    // process last block
    if (currentBlock.length > 0) {
        if (isOldBlock) {
            archiveLines.push(...currentBlock);
        } else {
            activeLines.push(...currentBlock);
        }
    }
    
    fs.writeFileSync(filePath, activeLines.join('\n'));
    if (archiveLines.length > headerLength) {
        fs.appendFileSync(archivePath, '\n' + archiveLines.slice(headerLength).join('\n'));
    }
    console.log(`Archived ${archiveLines.length - headerLength} lines from implementation log.`);
}

// ----- Arquivar 03-backlog.md -----
function archiveBacklog() {
    const filePath = path.join(memoryDir, '03-backlog.md');
    const archivePath = path.join(archivesDir, `03-backlog-archive-${archiveSuffix}.md`);
    
    if (!fs.existsSync(filePath)) return;
    
    const content = fs.readFileSync(filePath, 'utf8');
    const lines = content.split('\n');
    
    let activeLines = [];
    let archiveLines = [];
    
    let currentBlock = [];
    let isArchivableBlock = false;
    
    let isHeader = true;
    for (let i = 0; i < lines.length; i++) {
        const line = lines[i];
        if (line.startsWith('## Planejando') || line.startsWith('## Concluido') || line.startsWith('## Em execucao')) {
            isHeader = false;
        }
        
        if (isHeader) {
            activeLines.push(line);
            if (!fs.existsSync(archivePath)) {
                archiveLines.push(line);
            }
            continue;
        }
        
        if (line.startsWith('## ')) {
            // Process previous block
            if (currentBlock.length > 0) {
                if (isArchivableBlock) {
                    archiveLines.push(...currentBlock);
                } else {
                    activeLines.push(...currentBlock);
                }
            }
            
            // Start new block
            currentBlock = [line];
            isArchivableBlock = line.toLowerCase().includes('concluido');
        } else {
            currentBlock.push(line);
        }
    }
    
    // process last block
    if (currentBlock.length > 0) {
        if (isArchivableBlock) {
            archiveLines.push(...currentBlock);
        } else {
            activeLines.push(...currentBlock);
        }
    }
    
    fs.writeFileSync(filePath, activeLines.join('\n'));
    let headerLinesToSkip = 0;
    while(archiveLines[headerLinesToSkip] && !archiveLines[headerLinesToSkip].startsWith('## ')) {
        headerLinesToSkip++;
    }
    if (archiveLines.length > headerLinesToSkip) {
        fs.appendFileSync(archivePath, '\n' + archiveLines.slice(headerLinesToSkip).join('\n'));
    }
    console.log(`Archived backlog lines: ${archiveLines.length - headerLinesToSkip}.`);
}

archiveImplementationLog();
archiveBacklog();
console.log('Arquivamento concluído com sucesso!');
