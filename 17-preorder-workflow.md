# Pre-Order Workflow

---

## End-to-End Process Map

```
CUSTOMER PLACES ORDER (Shopify)
        │
        ▼
ORDER DATA → Shopify Order Management
        │
        ▼
DAILY BATCH EXPORT ──→ Spreadsheet / Order Dashboard
(via Shopify CSV export     (aggregate by design × size × color)
 or API integration)
        │
        ▼
BLANK SHIRT PROCUREMENT
(Pre-ordered in bulk from Gildan/Bella Canvas wholesaler)
Blanks already at Virginia printer or shipped to them
        │
        ▼
VIRGINIA PRINTER receives:
  - Design files (pre-loaded)
  - Daily print manifest (design × size × quantity)
  - Prints shirts (DTG or screen print depending on volume per design)
        │
        ▼
PRINTED SHIRTS ──→ PACK & SHIP
  Option A: Printer ships direct (if they offer fulfillment)
  Option B: Shirts sent to nearby 3PL for fulfillment
        │
        ▼
SHIPPING LABELS generated via:
  - ShipStation (connects to Shopify + USPS/UPS)
  - Or Shopify Shipping (built-in label generation)
        │
        ▼
TRACKING INFO ──→ Shopify automatically emails customer
  (via Shopify notifications or Klaviyo flow)
        │
        ▼
CUSTOMER RECEIVES SHIRT ✓
```

---

## Phase-by-Phase Detail

### Phase A: Pre-Orders Open (June 16 – July 14)
- **Shopify collects orders** via Pre-Order Manager app
- **Payment captured immediately** (not "pay later" — we need cash flow for blanks/printing)
- **Daily: export order data** → aggregate demand by design × size
- **Blanks procurement:** Order blanks in waves based on demand signals
  - Week 1-2: Order first batch (5K-10K units across sizes based on initial sales mix)
  - Week 3-4: Reorder based on actual sales data

### Phase B: Production (July 1 – July 21)
- **Send accumulated orders to Virginia printer** in batches
- **Print schedule:** Process largest-volume designs first
- **QC checkpoint:** Spot-check 5% of each batch before shipping
- **Target: all pre-orders printed by July 21** (10 days before release)

### Phase C: Fulfillment & Shipping (July 14 – July 28)
- **Ship in waves** as batches complete (don't wait for all orders)
- **First-come-first-served:** Earlier orders ship first
- **Cutoff date:** Last pre-orders accepted July 21 for guaranteed delivery by July 31
- **Shipping method:** USPS Priority Mail (2-3 day delivery) for most orders
- **Tracking emails** sent automatically via Shopify/Klaviyo

### Phase D: Post-Release (July 31 – August 7)
- **Remaining inventory** (if any) available for immediate purchase (not pre-order)
- **"Last Chance" messaging** — final sales push
- **Wind down:** Stop taking orders once inventory is depleted

---

## Tool Recommendations at Each Step

| Step | Tool | Why |
|---|---|---|
| **Order collection** | Shopify + Amai Pre-Order Manager | Enables pre-order flow with "ships by" date messaging |
| **Order aggregation** | Shopify Reports + Google Sheets | Export orders, pivot by design/size for production planning |
| **Blanks ordering** | Direct from wholesaler (see `18-blank-shirt-sourcing.md`) | Phone/email order with bulk pricing |
| **Print file management** | Google Drive / Dropbox shared with printer | Design files in print-ready format (300 DPI, correct dimensions) |
| **Print production** | Virginia printer (existing relationship) | DTG for < 500/design, screen print for > 500/design |
| **Shipping labels** | ShipStation ($25/mo for 500 labels) or Shopify Shipping | Bulk label generation, rate comparison, tracking sync |
| **Carrier** | USPS Priority Mail or UPS Ground | Priority for speed, Ground for cost on larger orders |
| **Tracking notifications** | Shopify native or Klaviyo email flows | Automatic tracking email when label is created |
| **Customer service** | Shopify Inbox (free) + email | Handle sizing questions, delivery inquiries |

---

## Key Decision: Ship from Printer vs. 3PL?

| Factor | Ship from Printer | Ship via 3PL |
|---|---|---|
| **Speed** | Fastest — no extra transit step | Adds 1-2 days for transfer |
| **Cost** | Depends on printer's fulfillment capability | $2.50-3.50/order (ShipBob/ShipMonk) |
| **Scalability** | Printers aren't fulfillment experts — may bottleneck at 1K+/day | 3PLs handle high volume easily |
| **Recommendation** | **Use for first 10K units** — test the flow | **Switch to 3PL if scaling past 50K** |

**Best approach:** Ask your Virginia printer if they can ship direct. If yes, start there. If volume exceeds their shipping capacity, bring in a 3PL.
